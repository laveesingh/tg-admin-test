from django.contrib import admin
from tours.models import Tour, TourMedia, TourReview
# Register your models here.

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    pass


@admin.register(TourMedia)
class TourMediaAdmin(admin.ModelAdmin):
    pass


@admin.register(TourReview)
class TourReviewAdmin(admin.ModelAdmin):

    list_display = ('rating', 'comment', 'tour')
    search_fields = ['rating', 'comment', 'tour__title']
    # prepopulated_fields = {'slug': ('rating', 'comment')}

