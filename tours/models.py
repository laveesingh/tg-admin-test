from django.db import models
# from tours.widgets import AdminImageWidget
# Create your models here.
CHAR_FIELD_MAX_LENGTH = 300

class Tour(models.Model):
    url = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH, default='')
    title = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH, default='')
    backend_id = models.IntegerField(default=0)
    description = models.TextField(default='')
    bookings = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class TourMedia(models.Model):
    category = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH, default='')
    title = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH, default='')
    image = models.ImageField(upload_to='media' ) #, widget=AdminImageWidget)
    tour_id = models.ForeignKey(Tour, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.category + ' : ' + self.title


class TourReview(models.Model):
    rating = models.IntegerField(default=0)
    comment = models.TextField(default='')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.rating) + ' : ' + self.comment