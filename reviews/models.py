from django.db import models
from tours.models import Tour


CHAR_FIELD_MAX_LENGTH = 300


class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(default='')

    def __str__(self):
        return str(self.rating) + ' : ' + self.comment
