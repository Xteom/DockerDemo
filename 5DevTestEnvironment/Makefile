IMAGE_NAME = tesseract-ocr
TAG = latest

.PHONY: build
build:
	docker build -t $(IMAGE_NAME):$(TAG) .

.PHONY: run
run:
	docker compose up -d

.PHONY: clean
clean:
	docker rmi $(IMAGE_NAME):$(TAG)