from celery import Celery

# app = Celery("tasks", broker="pyamqp://guest@localhost//")
app = Celery("tasks", backend="rpc://", broker="pyamqp://")

# https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html
app.conf.update(
    task_serializer="json",
    accept_content=["json"],  # Ignore other content
    result_serializer="json",
    timezone="Europe/Berlin",
    enable_utc=True,
)


@app.task
def add(x, y):
    return x + y
