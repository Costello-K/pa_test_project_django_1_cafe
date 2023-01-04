FROM python
MAINTAINER Kostiantyn Kondratenko

#ENV

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . .

EXPOSE 8000

#CMD ['python', 'manage.py', 'runserver']
CMD ['manage.py', 'runserver']
