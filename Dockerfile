# 베이스 이미지
FROM python:3.12-slim

# 환경 변수
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 작업 디렉토리
WORKDIR /app

# 필요 패키지 설치
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 프로젝트 복사
COPY . /app/

# 포트 오픈
EXPOSE 8000

# 서버 실행 전에 static 파일 모으기
CMD python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000


# 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

