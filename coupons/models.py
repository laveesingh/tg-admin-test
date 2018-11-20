from django.db import models
from orders.models import Order

CHAR_FIELD_MAX_LENGTH = 300


class Coupon(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    code = models.CharField(default='', max_length=CHAR_FIELD_MAX_LENGTH)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.code