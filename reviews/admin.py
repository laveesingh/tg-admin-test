from django.contrib import admin
from django.urls import path
from reviews.models import Review
from django.utils.html import format_html


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('comment', 'rating', 'tour', 'action')
    list_select_related = (
        'tour',
    )
    search_fields = ['comment', 'tour__title', 'rating']
    list_filter = ['rating', 'tour__title']
    change_list_template = "reviews/review_buttons.html"

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path(str(Review.id) + '/delete', self.delete__review),
            path(str(Review.id) + '/change', self.edit__review),
        ]
        return new_urls + urls

    def delete__review(self, request):
        pass

    def edit__review(self, request):
        pass

    @staticmethod
    def action(self):
        return format_html('<a class="button" style="background-color:red" href="%s">Delete</a>&nbsp;'
                           ' <a class="button" style="background-color:orange" href="%s">Edit</a>'
                           % (str(self.id) + '/delete', str(self.id) + '/change'))
