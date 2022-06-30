FROM python:3.10.4-alpine

WORKDIR .

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]