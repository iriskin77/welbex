import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

DATABASE_URI = f'postgres://{os.environ.get("POSTGRES_USER")}:' \
               f'{os.environ.get("POSTGRES_PASSWORD")}@' \
               f'{os.environ.get("POSTGRES_HOST")}:{os.environ.get("POSTGRES_PORT")}/' \
               f'{os.environ.get("POSTGRES_DB")}'

APPS_MODELS = [
    "cargo.models",
    "car.models",
    "location.models",
    "aerich.models",
]