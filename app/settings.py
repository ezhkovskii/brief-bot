"""Application settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8',  extra='ignore')

       
    # base kwargs
    DEBUG: bool = False

    BOT_TOKEN: str = ""

    # database
    POSTGRES_DSN: str = ""
    SQL_DEBUG: bool = False




settings = AppSettings()