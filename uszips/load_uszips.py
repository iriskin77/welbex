import pandas as pd
from location.models import Location
import psycopg2
from core.settings import POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD

uszips = pd.read_csv("/home/abc/Рабочий стол/welbex/uszips/uszips.csv")


async def load_uszips(uszips: pd.DataFrame) -> None:
    uszips_to_add = uszips[["zip","latitude","longitude","city","state"]]
    print(uszips_to_add.to_dict('records'))
    await Location.bulk_create([Location(**item) for item in uszips_to_add.to_dict('records')])


def test():
    conn = psycopg2.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
    )

    #cur = conn.cursor()
    with conn.cursor() as cursor:
        cursor.execute('''SELECT * FROM location''')
        print(cursor)


test()
