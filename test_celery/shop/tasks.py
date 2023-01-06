from time import sleep
from test_celery.celery import app
from celery import shared_task

@app.task()
@shared_task
def test_task(test_arg="Стандартный аргумент6"):
    sleep(10)
    print(f"ТЕСТОВАЯ ТАСКА {test_arg}")