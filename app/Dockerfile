FROM python:3.12.3-bookworm

WORKDIR /usr/src/app
ENV HOST 0.0.0.0
ENV PORT 8080

COPY . .

RUN pip install --no-cache-dir --upgrade -r /usr/src/app/requirements.txt


EXPOSE $PORT
CMD exec uvicorn --host $HOST --port $PORT main:app
