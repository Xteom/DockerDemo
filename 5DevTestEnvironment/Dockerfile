FROM ubuntu:22.04

RUN apt update

RUN apt install tesseract-ocr -y

COPY requirements.txt .

COPY app.py .

RUN pip install -r requirements.txt

ENTRYPOINT [ "gradio", "app.py" "--port", "7780"]