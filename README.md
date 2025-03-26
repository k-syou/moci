# 영화 추천 시스템 (Movie Recommendation System)

## 프로젝트 소개

이 프로젝트는 사용자의 선호도와 기분에 따라 영화를 추천해주는 웹 애플리케이션입니다. ML-100K 데이터셋을 기반으로 협업 필터링과 컨텐츠 기반 필터링을 결합한 하이브리드 추천 시스템을 구현했습니다.

## 주요 기능

- 영화 제목 기반 추천
- 장르 기반 추천
- 기분 기반 추천
- 랜덤 요소가 포함된 다양한 추천 결과

## 기술 스택

### 백엔드

- **Python 3.x**
- **Flask**: 웹 서버 프레임워크
- **pandas**: 데이터 처리 및 분석
- **numpy**: 수치 연산
- **scikit-learn**: 코사인 유사도 계산
- **requests**: HTTP 요청 처리

### 프론트엔드

- **React**: UI 프레임워크
- **Material-UI**: UI 컴포넌트 라이브러리
- **axios**: HTTP 클라이언트

## 프로젝트 구조

```
project/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── movie_routes.py
│   │   │   ├── genre_routes.py
│   │   │   └── mood_routes.py
│   │   ├── services/
│   │   │   ├── recommendation_service.py
│   │   │   └── data_service.py
│   │   └── models/
│   │       └── model.py
│   ├── data/
│   └── run.py
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── MovieSearch.js
    │   │   ├── GenreSearch.js
    │   │   └── MoodSearch.js
    │   └── App.js
    └── package.json
```

## 설치 및 실행 방법

### 백엔드 설정

1. 필요한 패키지 설치:

```bash
pip install -r requirements.txt
```

2. 모델 학습:

```bash
python backend/train.py
```

3. 서버 실행:

```bash
python backend/run.py
```

### 프론트엔드 설정

1. 필요한 패키지 설치:

```bash
cd frontend
npm install
```

2. 개발 서버 실행:

```bash
npm start
```

## API 엔드포인트

### 영화 제목 기반 추천

- **URL**: `/recommend/movie`
- **Method**: POST
- **Request Body**:

```json
{
    "title": "영화 제목"
}
```

### 장르 기반 추천

- **URL**: `/recommend/genre`
- **Method**: POST
- **Request Body**:

```json
{
    "genres": ["Action", "Drama", "Comedy"]
}
```

### 기분 기반 추천

- **URL**: `/recommend/mood`
- **Method**: POST
- **Request Body**:

```json
{
    "mood": "happy"
}
```

## 데이터셋

- ML-100K 데이터셋 사용
- 자동 다운로드 기능 포함
- 영화 정보 및 사용자 평점 데이터 포함

## 주요 기술적 특징

1. **하이브리드 추천 시스템**

   - 협업 필터링 (사용자-아이템 유사도)
   - 컨텐츠 기반 필터링 (장르 유사도)
2. **랜덤 요소 포함**

   - 추천 결과의 다양성 확보
   - 사용자 경험 향상
3. **모듈화된 구조**

   - 관심사 분리
   - 코드 재사용성
   - 유지보수 용이성
