import logging

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./.env",
        env_ignore_empty=True,
    )

    OPENAI_API_KEY: str


logging.basicConfig(
    level="INFO", format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p"
)
settings = Settings()
