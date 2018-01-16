from celery import Celery

app = Celery('add_task', broker='amqp://guest@localhost//', backend='rpc://')


# celery  -A add_task worker --pool=solo --loglevel=info

@app.task
def add(x, y):
    return x + y
