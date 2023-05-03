IMAGE_NAME = ml-api-fastapi-docker

.PHONY: build
build:
	docker build -t $(IMAGE_NAME) .

.PHONY: run
run:
	docker run --rm -p 8000:8000 $(IMAGE_NAME)

.PHONY: clean
clean:
	docker rmi $(IMAGE_NAME)