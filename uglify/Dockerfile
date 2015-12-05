FROM mhart/alpine-node:latest

ENV AUTH_KEY "keys1234"

MAINTAINER Moorthy RS "https://github.com/rsmoorthy"

RUN mkdir /app

COPY app.js package.json /app/

RUN cd /app; npm install .

EXPOSE 80

CMD ["node", "/app/app.js"]
