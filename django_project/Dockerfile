#Use python as parent image
FROM python:3.7

#Create environment
ENV PYTHONUNBUFFERED 1

RUN mkdir /django_project
WORKDIR /django_project
ADD . /django_project
COPY . requirements.txt
RUN pip install -r requirements.txt