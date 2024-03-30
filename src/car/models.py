from tortoise import models
from tortoise import fields


class Car(models.Model):
    """"Таблица car"""""

    id = fields.IntField(pk=True, unique=True)
    unique_number = fields.CharField(max_length=255)
    car_name = fields.CharField(max_length=255)
    load_capacity = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    car_location = fields.ForeignKeyField(
        'models.Location', related_name='car_location', on_delete=fields.SET_NULL, null=True
    )

    def __str__(self):
        return self.car_name
