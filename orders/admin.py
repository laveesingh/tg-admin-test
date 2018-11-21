from django.contrib import admin
from orders.models import Order
from django.utils.html import format_html
from django.urls import path


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['email', 'status', 'booking_reference', 'event_day', 'tour', 'action']
    list_select_related = (
        'tour',
    )
    search_fields = ['email', 'status', 'booking_reference', 'event_day']
    list_filter = ['email', 'status',  'event_day']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path(str(Order.id) + '/delete', self.delete__order),
            path(str(Order.id) + '/change', self.edit__order),
        ]
        return new_urls + urls

    def delete__order(self, request):
        pass

    def edit__order(self, request):
        pass

    @staticmethod
    def action(self):
        return format_html('<a class="button" style="background-color:red" href="%s">Delete</a>&nbsp;'
                           ' <a class="button" style="background-color:orange" href="%s">Edit</a>'
                           % (str(self.id) + '/delete', str(self.id) + '/change'))