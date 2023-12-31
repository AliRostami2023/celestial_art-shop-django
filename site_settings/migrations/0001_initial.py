# Generated by Django 4.2.6 on 2023-11-04 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLinkBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'لینک های فوتر',
                'verbose_name_plural': 'دسته بندی های لینک های فوتر',
            },
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=200, verbose_name='نام سایت')),
                ('site_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='دامنه سایت')),
                ('instagram', models.CharField(blank=True, max_length=200, null=True, verbose_name='اینستاگرام')),
                ('telegram', models.CharField(blank=True, max_length=200, null=True, verbose_name='تلگرام')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='ایمیل')),
                ('copy_right', models.TextField(blank=True, null=True, verbose_name='متن کپی رایت سایت')),
                ('about_us_text', models.TextField(blank=True, null=True, verbose_name='متن درباره ما سایت')),
                ('site_logo', models.ImageField(upload_to='uploads/logo_image', verbose_name='لوگو سایت')),
                ('is_main_setting', models.BooleanField(default=True, verbose_name='تنظیمات اصلی')),
            ],
            options={
                'verbose_name': 'تنظیمات',
                'verbose_name_plural': 'تنظیمات سایت',
            },
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url', models.URLField(max_length=500, verbose_name='لینک')),
                ('footer_link_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_settings.footerlinkbox', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'لینک فوتر',
                'verbose_name_plural': 'لینک های فوتر',
            },
        ),
    ]
