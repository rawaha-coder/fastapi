from pydantic_settings import BaseSettings

# change the values to match your reference
class Settings(BaseSettings):
    database_hostname: str  # to fill
    database_port: str  # to fill
    database_password: str  # to fill
    database_name: str  # to fill
    database_username: str # to fill
    secret_key: str # to fill
    algorithm: str  # to fill
    access_token_expire_minutes: int # to fill

    class Config:
        env_file = ".env"


settings = Settings()