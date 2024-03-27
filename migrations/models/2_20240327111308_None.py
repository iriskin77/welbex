from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "location" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "city" VARCHAR(255) NOT NULL,
    "state" VARCHAR(255) NOT NULL,
    "zip" INT NOT NULL,
    "latitude" DOUBLE PRECISION NOT NULL,
    "longitude" DOUBLE PRECISION NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "cargo" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "cargo_name" VARCHAR(255) NOT NULL,
    "weight" INT NOT NULL,
    "description" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "delivery_location_id" INT REFERENCES "location" ("id") ON DELETE SET NULL,
    "pick_up_location_id" INT REFERENCES "location" ("id") ON DELETE SET NULL
);
CREATE TABLE IF NOT EXISTS "car" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "unique_number" VARCHAR(255) NOT NULL,
    "car_name" VARCHAR(255) NOT NULL,
    "load_capacity" INT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "car_location_id" INT REFERENCES "location" ("id") ON DELETE SET NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
