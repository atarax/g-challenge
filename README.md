# Submission for challenge

## Requirements

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* [Minikube](https://minikube.sigs.k8s.io/)

## How to use

### Docker-Compose

* Assumes a free port 80
* With docker-compose: `docker-compose up`
* Run `scripts/test.sh` or directly in the container with pytest as usual

### Minikube

* Ensure minicube is running
* Run `scripts/deploy_minikube.sh`
* A link to openapi-docs will be displayed 

## Framework

* Dependency-Management with [Poetry](https://python-poetry.org/)
* Routing with [FastApi](https://fastapi.tiangolo.com/)
* ORM with [SQLAlchemy](https://www.sqlalchemy.org/)
* Type-Validation with [Pydantic](https://pydantic-docs.helpmanual.io/)
* Migrations with [Alembic](https://alembic.sqlalchemy.org/) 

Builds on top of a simplified version of:

* https://github.com/tiangolo/full-stack-fastapi-postgresql

## App

* OpenAPI-Docs can be found under `/docs`
* Demo-Data is available and the main endpoint is `/api/v1/products_in_store/`
* Basic CRUD-functionalities are available for all objects to provide rich 
  user experience :)
