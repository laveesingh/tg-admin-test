from django.db import models

CHAR_FIELD_MAX_LENGTH = 300

class Tour(models.Model):
    title = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH, default='')
    url = models.SlugField(max_length=CHAR_FIELD_MAX_LENGTH, default='', unique=True)

    def __str__(self):
        return self.title
