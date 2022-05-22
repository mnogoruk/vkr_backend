from functools import lru_cache

from app.core.settings.app import AppSettings


@lru_cache(10)
def get_app_settings() -> AppSettings:
    return AppSettings()
