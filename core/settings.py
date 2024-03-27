import os
from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_scoped_session
from asyncio import current_task

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")

DATABASE_URI = f'postgresql+asyncpg://{os.environ.get("POSTGRES_USER")}:' \
               f'{os.environ.get("POSTGRES_PASSWORD")}@' \
               f'{os.environ.get("POSTGRES_HOST")}:{os.environ.get("POSTGRES_PORT")}/' \
               f'{os.environ.get("POSTGRES_DB")}'




#DATABASE_URL_POSTGRES = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

#DATABASE_URL_SQLITE = f"sqlite+aiosqlite:///task_db.sqlite3"

engine = create_async_engine(DATABASE_URI, echo=False, future=True)
SessionLocal = sessionmaker(autoflush=False, bind=engine, class_=AsyncSession)
