from django.contrib import admin
from coupons.models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount', 'order']
    list_select_related = (
        'order',
    )
    search_fields = ['order__booking_reference', 'code', 'discount']
    list_filter = ['order__booking_reference', 'discount']
