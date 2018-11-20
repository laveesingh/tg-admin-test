from django.contrib import admin
from tours.models import Tour


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    pass
