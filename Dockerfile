FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1 #OUTPUT

WORKDIR src
COPY . /src
EXPOSE 8001
RUN pip install -r requirements.txt
CMD ["uvicorn","--host"."0.0.0.0","--port","80001","src.main:app"]