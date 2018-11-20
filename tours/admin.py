from django.contrib import admin
from tours.models import Tour


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'url',)
    search_fields = ['title', 'url']
    list_filter = ['title']

