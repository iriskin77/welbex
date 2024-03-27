import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_DB = os.environ.get("POSTGRES_DB")

# DATABASE_URI = f'postgres://{os.environ.get("POSTGRES_USER")}:' \
#                f'{os.environ.get("POSTGRES_PASSWORD")}@' \
#                f'{os.environ.get("POSTGRES_HOST")}:{os.environ.get("POSTGRES_PORT")}/' \
#                f'{os.environ.get("POSTGRES_DB")}'

DATABASE_URI = f'postgres://{POSTGRES_USER}:' \
               f'{POSTGRES_PASSWORD}@' \
               f'{POSTGRES_HOST}:{POSTGRES_PORT}/' \
               f'{POSTGRES_DB}'

APPS_MODELS = [
    "cargo.models",
    "car.models",
    "location.models",
    "aerich.models",
]

USZIPS_PATH = str(BASE_DIR) + "/load_data/uszips.csv"
