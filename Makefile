server:
	celery -A tasks worker --loglevel=INFO

start:
	python3 -m celeryconfig

flower:
	celery -A tasks worker flower

rabbit:
	sudo rabbitmq-server -detached