DOCKER_COMPOSE = docker-compose
CONTAINER_NAME = football_transfermarkt_backend

.PHONY: ruff ruff-fix test clean docker-start docker-build docker-shell docker-migrate docker-makemigrations

ruff:
	ruff .

ruff-fix:
	ruff --fix .

test:
	$(PYTHON) -m pytest

clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*.pyc" -type f -delete
	find . -name "*.pyo" -type f -delete

docker-start:
	$(DOCKER_COMPOSE) up --build

docker-build:
	$(DOCKER_COMPOSE) up -d --build

docker-shell:
	docker exec -it $(CONTAINER_NAME) bash

docker-migrate:
	docker exec -it $(CONTAINER_NAME) python manage.py migrate

docker-makemigrations:
	docker exec -it $(CONTAINER_NAME) python manage.py makemigrations
