#Use python as parent image
FROM python:3.7

#Create environment
ENV PYTHONUNBUFFERED 1
RUN mkdir /django_project
WORKDIR /django_project
#add file from local to container directory
COPY ./django_project/requirements.txt ./django_project/requirements.txt
ADD . /django_project
RUN pip install -r ./django_project/requirements.txt