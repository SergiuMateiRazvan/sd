import pydantic


class Settings(pydantic.BaseSettings):
    db_name: str = "students_internships_db"
    db_dsn: str = f"postgres://postgres:postgres@0.0.0.0:5432/{db_name}"
    queue_url: str = "0.0.0.0"
    queue_name: str = "Students-Descriptions"


settings = Settings()
