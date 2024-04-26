FROM python:3.10
LABEL authors="estebansanchez"

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]