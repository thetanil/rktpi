server:
	celery -A tasks worker

start:
	python3 -m celeryconfig