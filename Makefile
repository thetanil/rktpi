server:
	celery -A tasks worker --loglevel=INFO flower 

start:
	python3 -m celeryconfig

flower:
	celery -A tasks worker flower