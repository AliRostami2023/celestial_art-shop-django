from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.html import format_html


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, null=False, blank=True, unique=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'جزییات دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Product(models.Model):
    title = models.CharField(max_length=500, verbose_name='عنوان محصول')
    slug = models.SlugField(max_length=600, unique=True, null=False, blank=True, allow_unicode=True,
                            verbose_name='عنوان در url')
    category = models.ManyToManyField(to=Category, related_name='product_category', verbose_name='دسته بندی')
    price1 = models.IntegerField(verbose_name='قیمت')
    price2 = models.IntegerField(null=True, blank=True, verbose_name='قیمت بعد از تخفیف')
    images = models.ImageField(upload_to='uploads/orginal_image_product', null=True, blank=True,
                               verbose_name='تصویر اصلی محصول')
    color = models.CharField(max_length=200, null=True, blank=True, verbose_name='رنگ')
    size = models.CharField(max_length=200, null=True, blank=True, verbose_name='سایز')
    description = RichTextField(max_length=1000, verbose_name='توضیحات')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def show_image(self):
        return format_html('<img src = "{}" width=80% height=60px>'.format(self.images.url))

    class Meta:
        verbose_name = 'ثبت یا ویرایش محصول'
        verbose_name_plural = 'محصولات'


class ProductImage(models.Model):
    product = models.ForeignKey(to=Product, related_name='images_product', on_delete=models.CASCADE,
                                verbose_name='محصول')
    image = models.ImageField(upload_to='uploads/images_products', verbose_name='عکس محصول')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'عکس دیگر محصول'
        verbose_name_plural = 'سایر عکس های محصول'

    def image_tag(self):
        return format_html('<img src = "{}" width=60% height=110px>'.format(self.image.url))
