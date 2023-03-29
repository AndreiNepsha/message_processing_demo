import logging

import uvicorn

from src.apps.di_containers.app import AppContainer

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    container = AppContainer()
    container.wire(modules=["src.apps.api.dependencies"], packages=["src.infra.repositories"])
    container.init_resources()

    uvicorn.run(
        "src.apps.api.app:create_app",
        factory=True,
        host=container.config.api.host(),
        port=container.config.api.port(),
        log_config=container.telemetry.gunicorn_logging_dict(),
    )
