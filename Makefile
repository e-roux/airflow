include lib/makelib/common.mk
include lib/makelib/python.mk

IMAGE_NAME := apache/airflow:2.0.1-python3.8
DOCKER := docker
DOCKER_COMPOSE := docker-compose

# init {{{1
.PHONY: init
.env:
	@echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > $@

init: .env
	$(DOCKER_COMPOSE) up airflow-init
# 1}}}

# docker-compose {{{1
.PHONY: up
down:
	$(DOCKER_COMPOSE) $@

up: init
	$(DOCKER_COMPOSE) $@

compose.clean: down
	-$(DOCKER) volume rm airflow_postgres-db-volume
# 1}}}

clean: compose.clean

img:

requirements.txt:
	$(DOCKER) run --rm --entrypoint pip $(IMAGE_NAME) freeze > $@

# vim:fdm=marker:
