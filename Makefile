.PHONY: help postgres-start postgres-stop postgres-restart postgres-status postgres-logs postgres-psql

# Имя контейнера
CONTAINER_NAME = postgres-sync-async
# Имя образа
IMAGE = postgres:17
# Порт хоста
PORT_HOST = 5432
# Имя базы данных
DB_NAME = postgres
# Пользователь
DB_USER = postgres
# Пароль
DB_PASSWORD = postgres

help:
	@echo "Доступные команды:"
	@echo "  make postgres-start   - Запустить контейнер PostgreSQL"
	@echo "  make postgres-stop    - Остановить контейнер PostgreSQL"
	@echo "  make postgres-restart - Перезапустить контейнер PostgreSQL"
	@echo "  make postgres-status  - Показать статус контейнера"
	@echo "  make postgres-logs    - Показать логи контейнера"
	@echo "  make postgres-psql    - Подключиться к PostgreSQL через psql"

postgres-start:
	@echo "Запуск контейнера PostgreSQL..."
	@docker run -d \
		--name $(CONTAINER_NAME) \
		-e POSTGRES_PASSWORD=$(DB_PASSWORD) \
		-e POSTGRES_USER=$(DB_USER) \
		-e POSTGRES_DB=$(DB_NAME) \
		-p $(PORT_HOST):5432 \
		$(IMAGE) || \
	(docker start $(CONTAINER_NAME) && echo "Контейнер уже существует, запущен существующий")
	@echo "PostgreSQL запущен на порту $(PORT_HOST)"
	@echo "Подключение: host=localhost port=$(PORT_HOST) user=$(DB_USER) password=$(DB_PASSWORD) dbname=$(DB_NAME)"

postgres-stop:
	@echo "Остановка контейнера PostgreSQL..."
	@docker stop $(CONTAINER_NAME) 2>/dev/null || echo "Контейнер не запущен"
	@echo "Контейнер остановлен"

postgres-restart: postgres-stop postgres-start

postgres-status:
	@docker ps -a --filter name=$(CONTAINER_NAME) --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

postgres-logs:
	@docker logs $(CONTAINER_NAME)

postgres-psql:
	@docker exec -it $(CONTAINER_NAME) psql -U $(DB_USER) -d $(DB_NAME)

