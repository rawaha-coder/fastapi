from pydantic_settings import BaseSettings

# change the values to match your reference
class Settings(BaseSettings):
    database_hostname: str  = "localhost"
    database_port: str  = "5432"
    database_password: str  = "admin"
    database_name: str  = "fastapi"
    database_username: str = "postgres"
    secret_key: str = ""
    algorithm: str = ""
    access_token_expire_minutes: int = 32547716

    class Config:
        env_file = ".env"


settings = Settings()

