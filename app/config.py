from pydantic_settings import BaseSettings

# change the values to match your reference
class Settings(BaseSettings):
    database_hostname: str = "localhost" # to fill
    database_port: str = "5432" # to fill
    database_password: str = "admin" # to fill
    database_name: str = "fastapi" # to fill
    database_username: str = "postgres" # to fill
    secret_key: str = "" # to fill
    algorithm: str = "" # to fill
    access_token_expire_minutes: int = 23456443 # to fill

    class Config:
        env_file = ".env"


settings = Settings()