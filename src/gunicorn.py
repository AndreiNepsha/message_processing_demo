container = AppContainer()
container.init_resources()
container.wire(modules=["src.apps.task_queue.tasks"])

app_config = container.config


# Gunicorn values
bind = f"{app_config.service.api.host()}:{app_config.service.api.port()}"
logconfig_dict = container.telemetry.gunicorn_logging_dict()
worker_class = "uvicorn.workers.UvicornWorker"
wsgi_app = "src.apps.api.app:create_app()"
workers = app_config.service.http_workers_count()
