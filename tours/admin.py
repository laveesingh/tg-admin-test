from django.contrib import admin
from tours.models import Tour
from django.utils.html import format_html
from django.urls import path


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'action')
    search_fields = ['title', 'url']
    list_filter = ['title']
    prepopulated_fields = {'url': ('title', )}

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path(str(Tour.id) + '/delete', self.delete__tour),
            path(str(Tour.id) + '/change', self.edit__tour),
        ]
        return new_urls + urls

    def delete__tour(self, request):
        pass

    def edit__tour(self, request):
        pass

    @staticmethod
    def action(self):
        return format_html('<a class="button" style="background-color:red" href="%s">Delete</a>&nbsp;'
                           ' <a class="button" style="background-color:orange" href="%s">Edit</a>'
                           % (str(self.id) + '/delete', str(self.id) + '/change'))