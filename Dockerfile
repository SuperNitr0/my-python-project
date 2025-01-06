FROM python:3.9-slim

RUN apt-get update && apt-get install -y libpq-dev

WORKDIR /app

COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /app

EXPOSE 5000

CMD ["python", "app.py"]
