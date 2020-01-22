FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /project
WORKDIR /project/
COPY requirements.txt /project/
RUN pip install -r requirements.txt
ADD ./dj_project/ /project/