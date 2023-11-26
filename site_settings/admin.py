from django.contrib import admin
from site_settings.models import SiteSetting, FooterLink, FooterLinkBox, FAQ


# Register your models here.

class FooterLinkInline(admin.TabularInline):
    model = FooterLink



@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'instagram', 'telegram', 'email', 'logo', 'is_main_setting']


@admin.register(FooterLinkBox)
class FooterLinkBoxAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [FooterLinkInline]


# @admin.register(FooterLink)
# class FooterLinkAdmin(admin.ModelAdmin):
#     list_display = ['title', 'url', 'footer_link_box']


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'response', 'is_active']

