#Use python as parent image
FROM python:3.7

#Create environment
ENV PYTHONUNBUFFERED 1
COPY requirements.txt ./django_project
RUN mkdir /django_project
WORKDIR /django_project

ADD . /django_project
RUN pip install -r requirements.txt