from django.contrib import admin
from order_module.models import Order, OrderDetail, OrderCheckout


# Register your models here.

class OrderItemAdmin(admin.TabularInline):
    model = OrderDetail

class OrderCheckoutInline(admin.TabularInline):
    model = OrderCheckout


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_paid', 'payment_date', 'postal_tracking_code']
    list_filter = ['is_paid']
    search_fields = ['user']
    ordering = ['-id']
    inlines = [OrderItemAdmin , OrderCheckoutInline]


# @admin.register(OrderDetail)
# class OrderDetailAdmin(admin.ModelAdmin):
#     list_display = ['order', 'product', 'count', 'final_price']
#     search_fields = ['order', 'product']
#     ordering = ['-id']


# @admin.register(OrderCheckout)
# class OrderCheckoutAdmin(admin.ModelAdmin):
#     list_display = ['user', 'order', 'first_name', 'last_name', 'state', 'city', 'phone', 'sended']
#     search_fields = ['user', 'first_name', 'last_name', 'state', 'city']
#     list_filter = ['sended']
#     ordering = ['-id']
