from fastapi import FastAPI
import redis
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import os
import time

app = FastAPI()

# Environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "dockerlab")

# Redis client
redis_client = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

# Database connection
DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"
)

engine = create_engine(DATABASE_URL, future=True)


def create_visits_table():
    with engine.begin() as connection:
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS visits (
                id SERIAL PRIMARY KEY,
                visited_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """))


# Ensure database is ready and create table
def init_db():
    for attempt in range(10):
        try:
            create_visits_table()
            print("Database initialized successfully")
            return
        except Exception:
            print("Database not ready yet, retrying in 3 seconds...")
            time.sleep(3)

    print("Database initialization failed")


@app.on_event("startup")
def startup():
    init_db()


# Root endpoint with Redis caching
@app.get("/")
def read_root():
    cached = redis_client.get("homepage")

    if cached:
        return {"message": cached, "source": "redis-cache"}

    message = "Docker Essentials Lab running with caching"
    redis_client.set("homepage", message)

    return {"message": message, "source": "api"}


# Health endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}


# Redis connectivity test
@app.get("/redis")
def redis_test():
    try:
        redis_client.set("lab_message", "Redis is working")
        value = redis_client.get("lab_message")
        return {"redis_status": value}
    except Exception as e:
        return {"error": str(e)}


# PostgreSQL connectivity test
@app.get("/db")
def db_test():
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT 'Postgres is working' AS message;")
            )
            row = result.fetchone()
            return {"db_status": row[0]}
    except SQLAlchemyError as e:
        return {"error": str(e)}


# Track visits in database
@app.get("/visit")
def record_visit():
    try:
        # Safety net: ensure table exists even if startup timing was weird
        create_visits_table()

        with engine.begin() as connection:
            connection.execute(text("INSERT INTO visits DEFAULT VALUES"))
            result = connection.execute(text("SELECT COUNT(*) FROM visits"))
            count = result.scalar()

        return {"total_visits": count}

    except SQLAlchemyError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}