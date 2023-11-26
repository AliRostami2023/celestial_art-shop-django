from django.urls import path
from . import views

urlpatterns = [
    path('add-product-to-order-me/', views.add_product_to_order, name='add-product-to-order-me'),
    path('order-me/', views.user_basket, name='order-me-page'),
    path('remove-order-detail/', views.remove_order_detail, name='remove-order-page'),
    path('change-order-detail/', views.change_order_detail_count, name='change-order-page'),
    path('order-me/checkout/', views.CheckOutView.as_view(), name='checkout-page'),
    path('request-payment/', views.request_payment, name='request_payment'),
    path('verify-payment/', views.verify_payment, name='verify_payment'),
]

