from tortoise import models
from tortoise import fields


class Location(models.Model):
    """"Таблица location для адресов из uszips.csv"""""

    id = fields.IntField(pk=True, unique=True)
    city = fields.CharField(max_length=255)
    state = fields.CharField(max_length=255)
    zip = fields.IntField(unique=True)
    latitude = fields.FloatField()
    longitude = fields.FloatField()
    created_at = fields.DatetimeField(auto_now_add=True)



