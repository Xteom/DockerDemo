FROM python:3.8-slim

RUN apt update

RUN apt install tesseract-ocr -y

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

ENTRYPOINT [ "gradio", "app.py" ]