IMAGE_NAME = hello-docker-data-scientists

.PHONY: build
build:
	docker build -t $(IMAGE_NAME) .

.PHONY: run
run:
	docker run --rm $(IMAGE_NAME)

.PHONY: clean
clean:
	docker rmi $(IMAGE_NAME)