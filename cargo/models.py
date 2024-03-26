from tortoise import models
from tortoise import fields


class Cargo(models.Model):

    id = fields.IntField(pk=True, unique=True)
    cargo_name = fields.CharField(max_length=255)
    pick_up_cargo = fields.CharField(max_length=255)
    delivery_cargo = fields.CharField(max_length=255)
    weight = fields.IntField()
    description = fields.TextField()
    created_at = fields.DatetimeField()

    def __str__(self):
        return self.cargo_name
