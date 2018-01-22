FROM python:3-slim

RUN pip install --no-cache \
  coverage==4.4.2 \
  ansicolors==1.1.8 \
  twine==1.9.1

ENV PYTHONUNBUFFERED 1
