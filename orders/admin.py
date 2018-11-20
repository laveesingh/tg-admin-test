from django.contrib import admin
from orders.models import  Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
    # list_display = ('rating', 'comment', 'tour')
    # search_fields = ['rating', 'comment', 'tour__title']
    # prepopulated_fields = {'slug': ('rating', 'comment')}
