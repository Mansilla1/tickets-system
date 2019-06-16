FROM python:2
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /home/projects/challenge
RUN apt-get update
WORKDIR /home/projects/challenge
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
