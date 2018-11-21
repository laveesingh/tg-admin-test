from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from reviews.models import Review


def set_rating_to_zero(self, request, queryset):
    for review in queryset:
        review.rating = 0
        review.save()


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('comment', 'rating', 'tour')
    list_select_related = (
        'tour',
    )
    search_fields = ['comment', 'tour__title', 'rating']
    list_filter = ['rating', 'tour__title']
    # actions = [set_rating_to_zero, ]

    change_list_template = "reviews/review_buttons.html"

    def get_actions(self, request):
        actions = super().get_actions(request)

        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path('delete/', self.bulk_delete),
        ]
        return new_urls + urls

    def bulk_delete(self, request):
        self.model.objects.all().delete()
        self.message_user(request, "all reviews have been deleted")
        return HttpResponseRedirect('../')