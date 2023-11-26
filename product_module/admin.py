from django.contrib import admin
from . import models


# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = models.ProductImage


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price1', 'price2', 'show_image', 'color', 'size', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title']
    ordering = ['-id']
    inlines = [ProductImageInline]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'is_active']
    ordering = ['-id']


# @admin.register(models.ProductImage)
# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ['product', 'image_tag']
#     ordering = ['-id']
