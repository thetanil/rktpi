from celery import Celery

# app = Celery("tasks", broker="pyamqp://guest@localhost//")
app = Celery("tasks", backend="rpc://", broker="pyamqp://")

# https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html
app.config_from_object("celeryconfig")


@app.task
def add(x, y):
    return x + y
