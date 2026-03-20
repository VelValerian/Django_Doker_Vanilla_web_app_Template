# 🌀 NOMONDAYS INFRASTRUCTURE MAKEFILE (V2.0)

.PHONY: help build up down restart logs shell migrate manage test test-html

help:
	@echo "Доступные команды:"
	@echo "  make build         - Собрать/пересобрать Docker-образы"
	@echo "  make up            - Запустить контейнеры в фоне"
	@echo "  make down          - Остановить и удалить контейнеры"
	@echo "  make restart       - Перезагрузить сервисы"
	@echo "  make logs          - Просмотр логов"
	@echo "  make shell         - Зайти в shell контейнера web"
	@echo "  make migrate       - Применить миграции БД"
	@echo "  make manage ARGS=\"\" - Запустить manage.py (например, make manage ARGS=\"createsuperuser\")"
	@echo "  make test          - Запустить тесты с отчетом покрытия (Coverage)"
	@echo "  make test-html     - Запустить тесты и открыть отчет покрытия в браузере"

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

restart:
	docker compose restart

logs:
	docker compose logs -f

shell:
	docker compose exec web bash

migrate:
	docker compose exec web python web/manage.py migrate

manage:
	docker compose exec web python web/manage.py $(ARGS)

test:
	docker compose exec web pytest

test-html:
	docker compose exec web pytest --cov-report=html
