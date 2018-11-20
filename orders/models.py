from django.db import models
from tours.models import Tour


CHAR_FIELD_MAX_LENGTH = 300


class Order(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    email = models.EmailField()
    booking_reference = models.CharField(default='', max_length=CHAR_FIELD_MAX_LENGTH)
    event_day = models.DateField()
    people = models.IntegerField(default=0)
    status = models.CharField(max_length=1, choices=[
        ['c', 'confirmed'],
        ['p', 'pending'],
        ['o', 'open']
    ])

    def __str__(self):
        return self.booking_reference