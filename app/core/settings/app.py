import logging
from typing import Any, Dict, List, Tuple

from pydantic import BaseSettings


class AppSettings(BaseSettings):
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "VKR"
    version: str = "0.0.1"

    database_url: str = 'postgresql+asyncpg://user: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@95.163.214.31/PostgreSQL-2280'

    max_connection_count: int = 10
    min_connection_count: int = 10

    api_prefix = '/v1'

    allowed_hosts: List[str] = ["*"]

    logging_level: int = logging.INFO
    loggers: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    class Config:
        validate_assignment = True

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }
