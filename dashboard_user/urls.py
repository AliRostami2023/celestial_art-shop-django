from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardUser.as_view(), name='dashboard-user-page'),
    path('change-password-user/', views.ChangePasswordUser.as_view(), name='change-password-user-page'),
    path('shopping-user/', views.MyShopping.as_view(), name='shopping-user-page'),
    path('shopping-user/<order_id>', views.my_shopping_detail, name='detail-shopping-user-page'),
]
