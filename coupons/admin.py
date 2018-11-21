from django.contrib import admin
from coupons.models import Coupon
from django.utils.html import format_html
from django.urls import path


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    # configurations options
    actions_on_bottom = True
    # it also takes a callable for customized column name and value
    list_display = ['code', 'discount', 'order', 'action']
    list_select_related = ('order', )
    search_fields = ['order__booking_reference', 'code', 'discount']
    list_filter = ['order__booking_reference', 'discount']

    list_display_links = ['code', 'discount']
    autocomplete_fields = ['order']
    list_per_page = 8

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path(str(Coupon.id) + '/delete', self.delete__coupon),
            path(str(Coupon.id) + '/change', self.edit__coupon),
        ]
        return new_urls + urls

    def delete__coupon(self, request):
        pass

    def edit__coupon(self, request):
        pass

    @staticmethod
    def action(self):
        return format_html('<a class="button" style="background-color:red" href="%s">Delete</a>&nbsp;'
                           ' <a class="button" style="background-color:orange" href="%s">Edit</a>'
                           % (str(self.id) + '/delete', str(self.id) + '/change'))