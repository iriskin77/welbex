from tortoise import models
from tortoise import fields


class Car(models.Model):

    id = fields.IntField(pk=True, unique=True)
    unique_number = fields.CharField(max_length=255)
    car_name = fields.CharField(max_length=255)
    location = fields.CharField(max_length=255)
    load_capacity = fields.IntField()

    def __str__(self):
        return self.car_name
