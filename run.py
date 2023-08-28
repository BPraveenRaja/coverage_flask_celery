from factory import create_app
from celeryapp import celeryInstance

if __name__ == "__main__":
    app = create_app(celery=celeryInstance)
    app.run()
