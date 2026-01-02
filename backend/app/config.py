from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # LangSmith
    LANGSMITH_ENDPOINT: str
    LANGSMITH_API_KEY: str
    LANGSMITH_TRACING: bool = True
    LANGSMITH_PROJECT: str | None = None

    # Rely on process environment (direnv) in dev; avoid loading .env here
    model_config = SettingsConfigDict()

settings = Settings()