from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField


# Create your models here.


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, null=True, blank=True, verbose_name='دامنه سایت')
    instagram = models.CharField(max_length=200, null=True, blank=True, verbose_name='اینستاگرام')
    telegram = models.CharField(max_length=200, null=True, blank=True, verbose_name='تلگرام')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='ایمیل')
    copy_right = models.TextField(null=True, blank=True, verbose_name='متن کپی رایت سایت')
    text_header = models.TextField(null=True, blank=True, verbose_name='متن بالای صفحه')
    show_text_to_user = RichTextField(verbose_name='متن نمایش دهنده به کاربر در پروفایل')
    about_us_text = models.TextField(null=True, blank=True, verbose_name='متن درباره ما سایت')
    site_logo = models.ImageField(upload_to='uploads/logo_image', verbose_name='لوگو سایت')
    is_main_setting = models.BooleanField(default=True, verbose_name='تنظیمات اصلی')

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات سایت'

    def logo(self):
        return format_html('<img src = "{}" width=100% height=40px>'.format(self.site_logo.url))

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        verbose_name = 'لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, null=True, blank=True, verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=3000, verbose_name='سوال')
    response = models.TextField(verbose_name='پاسخ')
    is_active = models.BooleanField(default=True, verbose_name='منتشر شود / نشود')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'سوال و پاسخ'
        verbose_name_plural = 'سوالات متدوال'
