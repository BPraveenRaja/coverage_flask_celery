from celeryapp import celeryInstance
from factory import create_app
from celery_utils import init_celery

app = create_app()
init_celery(celeryInstance, app)
