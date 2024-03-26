from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "cargo" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "cargo_name" VARCHAR(255) NOT NULL,
    "pick_up_cargo" VARCHAR(255) NOT NULL,
    "delivery_cargo" VARCHAR(255) NOT NULL,
    "weight" INT NOT NULL,
    "description" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL
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
