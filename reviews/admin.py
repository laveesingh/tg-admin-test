from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('comment', 'rating', 'tour')
    list_select_related = (
        'tour',
    )
    search_fields = ['comment', 'tour__title', 'rating']
    list_filter = ['rating', 'tour__title']
