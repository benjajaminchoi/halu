# RAG Hallucination Detection and Classification System

## 프로젝트 소개 🌟
서울대학교 빅데이터 핀테크 AI 전문가 과정 캡스톤 프로젝트의 일환으로 수행된 프로토타입입니다.
AI 모델의 응답에서 발생할 수 있는 할루시네이션(환각, 허구)을 평가하고 분석하는 시스템을 구현했습니다. 
이는 8 Failure Types of LLM Output이라는 이론적 프레임워크를 기반으로 구현된 시스템입니다.
GPT-4를 활용하여 AI 응답의 신뢰성을 검증하고, 할루시네이션 여부를 판단하는 것을 목표로 합니다.

## 데이터셋 구축 📊
### 보험 도메인 특화 데이터셋
본 프로젝트는 보험 도메인에 특화된 고품질 데이터셋을 구축하여 할루시네이션 탐지의 정확도를 높였습니다.

#### 데이터셋 구축 과정
1. **Document 준비**
   - KB 착한암보험 무배당 약관을 기반 문서로 선정
   - 보험 전문 지식이 필요한 도메인 특화 데이터 구축

2. **전문가 Seed Data 생성**
   - 전문가가 50개의 기초 데이터(Question, Context, Answer) 생성
   - 보험 약관의 핵심 내용을 포괄하는 질의응답 쌍 구성

3. **Seed-based Data 확장**
   - 초기 50개의 Seed Data를 기반으로 200개의 추가 데이터 생성
   - 다양한 질문 유형과 맥락을 포함하도록 확장

4. **Hallucinated Answer 생성**
   - 기존 Question과 Context를 활용하여 의도적인 할루시네이션 응답 생성
   - 다양한 유형의 할루시네이션 포함 (Type 5~8)

5. **전문가 검수**
   - 생성된 모든 데이터에 대한 전문가 검증
   - 할루시네이션 유형 분류의 정확성 확인
   - 보험 도메인 전문성 검증

6. **Golden Dataset 완성**
   - 총 250개의 고품질 QA 쌍 구축
   - 할루시네이션 유형별 분류 정보 포함
   - 보험 도메인 특화 검증 데이터셋 확보

#### 데이터셋 구조
- **Question**: 보험 관련 질문
- **Context**: 관련 약관 내용 또는 배경 정보
- **Response**: AI 모델의 응답
- **is_hallucination**: 할루시네이션 여부
- **hallucination_type**: 할루시네이션 유형 분류 (Type 5~8)

## 주요 기능 💡
- AI 응답의 할루시네이션 평가: Type 5 (Irrelevance of LLM Output), Type 6 (Factual Contradiction), Type 7 (Factual Fabrication), Type 8 (Logical Inconsistency) 여부를 탐지하고 어떤 Type의 Hallucination인지 분류
- 실시간 응답 분석
- 웹 기반 사용자 인터페이스
- JSON 형식의 평가 결과 제공

## 기술 스택 🛠
- **Backend**: FastAPI, Python
- **Frontend**: HTML, JavaScript
- **AI 모델**: OpenAI GPT-4
- **템플릿 엔진**: Jinja2
- **배포**: Vercel, Docker

## 설치 방법 ⚙️
1. 저장소 클론
```bash
git clone https://github.com/benjajaminchoi/halu.git
cd halu
```

2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 의존성 패키지 설치
```bash
pip install -r requirements.txt
```

4. OpenAI API 키 설정
```bash
export OPENAI_API_KEY='your-api-key-here'
```

## 사용 방법 📝
1. 서버 실행
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

2. 웹 브라우저에서 접속
```
http://localhost:8000
```

## API 엔드포인트 📚
- `GET /`: 메인 웹 인터페이스
- `POST /evaluate`: 할루시네이션 평가
  - Request Body:
    ```json
    {
      "question": "사용자 질문",
      "context": "참조 컨텍스트(선택사항)",
      "response": "AI 응답"
    }
    ```
  - Response:
    ```json
    {
      "is_hallucination": boolean,
      "explanation": "평가 설명"
    }
    ```

## 프로젝트 구조 📂
```
halu/
├── app.py              # FastAPI 애플리케이션
├── prompt/            # 프롬프트 템플릿
│   └── one_eval.txt   # 평가 프롬프트
├── templates/         # HTML 템플릿
│   └── index.html     # 메인 페이지
├── requirements.txt   # 의존성 패키지
├── Dockerfile        # 도커 설정
└── vercel.json       # Vercel 배포 설정
```

## 개발 환경 설정 🔧
### Docker 사용
```bash
docker build -t halu .
docker run -p 8000:8000 -e OPENAI_API_KEY='your-api-key' halu
```

### Vercel 배포
- Vercel CLI 설치
```bash
npm i -g vercel
```
- 배포
```bash
vercel
```

## 기여 방법 🤝
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 라이선스 ⚖️
이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 연락처 📧
- 개발자: Benjamin Choi
- 웹사이트: halu-lilac.vercel.app
