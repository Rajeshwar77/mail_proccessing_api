from pydantic import BaseSettings
from functools import lru_cache


class AppSettings(BaseSettings):
    db_url: str
    app_name: str
    
    class Config:
        env_file = ".env.local"


@lru_cache
def get_settings():
    return AppSettings()

get_settings.cache_clear()
settings = get_settings()