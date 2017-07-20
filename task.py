# celery_example/tasks.py
from cornershop.celery_app import app


@app.task
def prueba_suma(x, y):
    return x + y


@app.task
def prueba_resta(x, y):
    return x - y