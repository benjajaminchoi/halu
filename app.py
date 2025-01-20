from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, field_validator
from openai import OpenAI
import json
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

client = OpenAI()


class EvaluationRequest(BaseModel):
    question: str
    context: str | None = ""  # Change default to empty string
    response: str

    @field_validator("context")
    def validate_context(cls, v):
        if v is None or v.strip() == "":
            return ""  # Return empty string instead of None
        return v.strip()


def get_prompt(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read()


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/evaluate")
async def evaluate_hallucination(evaluation: EvaluationRequest):
    try:
        input_data = {
            "question": evaluation.question,
            "response": evaluation.response,
        }

        if evaluation.context:
            input_data["context"] = evaluation.context

        input_text = json.dumps(input_data)
        system_prompt = get_prompt("prompt/one_eval.txt")

        # Add format enforcement to system prompt
        system_prompt += '\nIMPORTANT: Your response must be valid JSON with the following structure: {"is_hallucination": boolean, "explanation": string}'

        completion = client.chat.completions.create(
            model="gpt-4o",  # Fixed model name
            # temperature=0.1,  # Add lower temperature for more consistent formatting
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": input_text},
            ],
        )

        answer = completion.choices[0].message.content
        print(f"Raw OpenAI Response: {answer}")

        # Clean the response - remove any markdown formatting if present
        answer = answer.strip()
        if answer.startswith("```json"):
            answer = answer[7:]
        if answer.endswith("```"):
            answer = answer[:-3]
        answer = answer.strip()

        if not answer:
            raise HTTPException(status_code=500, detail="Empty response from AI")

        try:
            result = json.loads(answer)
            if not isinstance(result, dict) or "is_hallucination" not in result:
                raise HTTPException(
                    status_code=500, detail="Invalid response structure from AI"
                )
            return result
        except json.JSONDecodeError as je:
            print(f"JSON Parse Error: {str(je)}")
            print(f"Failed to parse: {answer}")
            raise HTTPException(status_code=500, detail="Invalid JSON response from AI")

    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
