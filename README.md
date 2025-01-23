# HALU (할루) - 데이터 기반 할루시노겐 분석 프로젝트

## 프로젝트 소개 🌟
HALU는 할루시노겐 관련 데이터를 분석하고 시각화하는 웹 기반 플랫폼입니다. 이 프로젝트는 데이터 사이언스와 웹 기술을 결합하여 의미 있는 인사이트를 도출하는 것을 목표로 합니다.

## 주요 기능 💡
- 데이터 분석 및 시각화
- 대화형 웹 인터페이스
- 실시간 데이터 처리
- 맞춤형 리포트 생성

## 기술 스택 🛠
- **Backend**: Python, Flask
- **Frontend**: HTML, JavaScript
- **데이터 처리**: Pandas, NumPy
- **시각화**: Matplotlib, Seaborn
- **배포**: Vercel

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

## 사용 방법 📝
1. 서버 실행
```bash
python app.py
```

2. 웹 브라우저에서 접속
```
http://localhost:5000
```

## 프로젝트 구조 📂
```
halu/
├── app.py              # Flask 애플리케이션 메인 파일
├── dataset.csv         # 분석용 데이터셋
├── templates/          # HTML 템플릿
├── prompt/            # 프롬프트 관련 파일
├── requirements.txt    # 의존성 패키지 목록
└── test.ipynb         # 테스트 및 개발용 노트북
```

## 데이터 분석 기능 📊
- 기술 통계 분석
- 시계열 데이터 분석
- 상관관계 분석
- 데이터 시각화

## API 문서 📚
- GET /api/data: 전체 데이터셋 조회
- POST /api/analyze: 데이터 분석 요청
- GET /api/visualize: 시각화 결과 조회

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

## 업데이트 내역 🔄
- v1.0.0 (2024-03)
  - 초기 버전 릴리스
  - 기본 분석 기능 구현
  - 웹 인터페이스 구축