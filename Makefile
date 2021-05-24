init:
	docker-compose up --build -d
up:
	docker-compose up -d
	make exec
down:
	docker-compose down
exec:
	docker exec -it interview-assessment python ./app.py
logs:
	docker-compose logs -f