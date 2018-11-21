from django.contrib import admin
from coupons.models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    # configurations options
    actions_on_bottom = True
    # it also takes a callable for customized column name and value
    list_display = ['code', 'discount', 'order']
    list_select_related = ('order', )
    search_fields = ['order__booking_reference', 'code', 'discount']
    list_filter = ['order__booking_reference', 'discount']

    list_display_links = ['code', 'discount']
    autocomplete_fields = ['order']
    list_per_page = 8
