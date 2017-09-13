FROM python:alpine

MAINTAINER https://github.com/rsmoorthy

RUN mkdir /app && mkdir /app/pql

COPY pql /app/pql/

RUN pip install dateutils && pip install bson

COPY web.py /app/
WORKDIR /app

EXPOSE 80

CMD ["python", "/app/web.py"]
