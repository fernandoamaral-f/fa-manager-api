from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    caminho_banco: str = "fa_manager.db"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()