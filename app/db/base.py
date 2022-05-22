from typing import Any

from sqlalchemy.ext.declarative import as_declarative

class_registry: dict = {}


@as_declarative(class_registry=class_registry)
class Base:
    __table_args__ = {"schema": "vkr"}

    id: Any
    __name__: str


Base.metadata.schema = 'metrics'
