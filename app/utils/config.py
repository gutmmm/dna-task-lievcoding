from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    data_dir: Path = Path("data/documents")
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    model_name: str = "gpt-4o-mini"


settings = Settings()
