FROM python:3.13.0-alpine3.19
RUN apk add --no-cache bash
RUN mkdir /app
RUN adduser --disabled-password runner
RUN chown -cR runner:runner /app
USER runner
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .