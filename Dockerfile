FROM python:3-slim

RUN pip install --no-cache \
  coverage==4.4.2 \
  ansicolors==1.1.8

ENV PYTHONUNBUFFERED 1
