from tortoise import models
from tortoise import fields


class Cargo(models.Model):
    """"Таблица cargo"""""

    id = fields.IntField(pk=True, unique=True)
    cargo_name = fields.CharField(max_length=255)
    weight = fields.IntField()
    description = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    pick_up_location = fields.ForeignKeyField(
        'models.Location', related_name='pick_up', on_delete=fields.SET_NULL, null=True
    )
    delivery_location = fields.ForeignKeyField(
        'models.Location', related_name='delivery', on_delete=fields.SET_NULL, null=True
    )

    def __str__(self):
        return self.cargo_name

