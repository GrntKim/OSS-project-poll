# docker 이미지
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app
# 요구사항 설치
RUN pip install --no-cache-dir Django==4.2.23
# 프로젝트 폴더 복사
COPY . .
# 8000 포트 열기
EXPOSE 8000
# 서버 동작 명령어
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]