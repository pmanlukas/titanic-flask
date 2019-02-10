#Dockerfile with multistage build
FROM python:3.7

LABEL maintainer="lukas.pollmann@outlook.com"

COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

RUN mkdir /app
WORKDIR /app

COPY . /app

EXPOSE 8080

ENTRYPOINT [ "python" ]
CMD [ "form.py" ]