from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "car" DROP COLUMN "city";
        ALTER TABLE "car" DROP COLUMN "state";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "car" ADD "city" VARCHAR(255) NOT NULL;
        ALTER TABLE "car" ADD "state" VARCHAR(255) NOT NULL;"""
