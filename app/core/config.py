from pydantic_settings import BaseSettings # import BaseSettings from pydantic_settings


# create settings class:
class Settings(BaseSettings):

    # database settings:
    POSTGRES_HOST: str # postgres host
    POSTGRES_PORT: int # postgres port

    POSTGRES_DB: str # postgres database
    POSTGRES_USER: str # postgres user
    POSTGRES_PASSWORD: str # postgres password

    # jwt settings:
    SECRET_KEY: str # secret key
    ALGORITHM: str # algorithm

    ACCESS_TOKEN_EXPIRE_MINUTES: int # access token expire minutes

    # config class:
    class Config:
        env_file = ".env" # env file


# create settings instance:
settings = Settings()