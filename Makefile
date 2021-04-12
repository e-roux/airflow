include lib/makelib/common.mk
include lib/makelib/python.mk


IMAGE_NAME := apache/airflow:2.0.1-python3.8

img:

requirements.txt:
	$(DOCKER) run --rm --entrypoint pip $(IMAGE_NAME) freeze > $@
