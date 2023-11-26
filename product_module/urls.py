from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='product-list'),
    path('cat/<cat>', views.ProductList.as_view(), name='category-list-object-page'),
    path('<slug>/', views.ProductDetail.as_view(), name='product-detail'),
]
