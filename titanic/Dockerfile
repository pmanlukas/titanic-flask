#Dockerfile with multistage build
FROM python:3.7

LABEL maintainer="lukas.pollmann@outlook.com"

COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

RUN mkdir /app
COPY model_cols.pkl /app
COPY model.pkl /app
COPY api.py /app

WORKDIR /app

EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD [ "api.py" ]