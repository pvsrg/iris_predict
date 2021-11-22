FROM python:3.8-slim

COPY . ./root

WORKDIR /root

RUN pip install flask gunicorn numpy pandas sklearn scipy joblib flask_wtf