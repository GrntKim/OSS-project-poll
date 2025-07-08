# OSS Project Poll


## 프로젝트 개요

이 프로젝트는 오픈소스 프로젝트에 대한 투표 시스템을 구현한 웹 애플리케이션입니다. 사용자들이 프로젝트를 평가하고 평점을 매길 수 있습니다.

## 주요 기능

1.  **프로젝트 목록 조회**
    - 등록된 모든 프로젝트 목록 확인

2.  **프로젝트 상세 정보**
    - 프로젝트명, 제작자, 상세 내용 확인

3.  **평점 투표**
    - 1-5점 척도로 프로젝트 평가

4.  **투표 결과**
    - 실시간 투표 결과 및 통계 확인

5. ️ **관리자 기능**: 
    - Django Admin을 통한 프로젝트 관리
    - 투표율 높은 순으로 프로젝트 목록 열람 가능

## 기술 스택

- **Backend**: Django 4.2.23
- **Frontend**: HTML5, CSS3
- **Database**: SQLite3
- **Container**: Docker
- **Language**: Python 3.11

## 설치 및 실행

### 사전 요구사항

- Docker
- Docker Compose

### 사용 방법

```bash
# 저장소 클론
git clone https://github.com/GrntKim/OSS-project-poll.git
cd OSS-project-poll

# 첫 실행 (빌드 포함)
docker-compose up --build -d

# 이후 실행
docker-compose up -d

# 중지
docker-compose down
```


## 접속 주소

- **어플리케이션 페이지**: http://localhost:8000/polls
- **관리자 페이지**: http://localhost:8000/admin

## 기본 관리자 계정
- **Username**: `admin`
- **Password**: `admin123`
- **Email(입력 불필요)**: `admin@example.com`