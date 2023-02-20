FROM python:3.11-alpine

WORKDIR /app

COPY requirements-docker.txt ./requirements.txt

RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip install --no-cache-dir -r requirements.txt
RUN apk --purge del .build-deps

COPY . .

CMD ["python", "app.py"]
