init:
	sudo docker-compose up --build -d
	make exec
up:
	sudo docker-compose up -d
	make exec
down:
	sudo docker-compose down
exec:
	sudo docker exec -it interview-assessment bash
logs:
	sudo docker-compose logs -f