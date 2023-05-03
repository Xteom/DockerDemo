IMAGE_NAME = jupyterlab-docker-data-scientists

.PHONY: build
build:
	docker build -t $(IMAGE_NAME) .

.PHONY: run
run:
	docker run --rm -p 8888:8888 -v "$(shell pwd)/notebooks:/home/jovyan/notebooks" $(IMAGE_NAME)

.PHONY: clean
clean:
	docker rmi $(IMAGE_NAME)