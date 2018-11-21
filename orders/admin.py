from django.contrib import admin
from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['email', 'status', 'booking_reference', 'event_day', 'tour']
    list_select_related = (
        'tour',
    )
    search_fields = ['email', 'status', 'booking_reference', 'event_day']
    list_filter = ['email', 'status',  'event_day']