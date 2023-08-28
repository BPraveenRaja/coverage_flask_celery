def init_celery(celery, app):
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        def __call__(*args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(*args, **kwargs)
    celery.Task = ContextTask
