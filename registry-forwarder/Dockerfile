FROM elyase/pyrun:2.7
#FROM elyase/staticpython

MAINTAINER https://github.com/rsmoorthy

ENV REGISTRY_HOST "172.17.42.1"
ENV REGISTRY_PORT "5000"

RUN mkdir /app

COPY forward.py /app/

EXPOSE 5000

CMD ["python", "/app/forward.py"]
