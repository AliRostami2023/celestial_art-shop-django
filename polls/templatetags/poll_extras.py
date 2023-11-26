from django import template
from jalali_date import date2jalali

register = template.Library()


@register.filter(name='three_digits_currency')
def three_digits_currency(value):
    return '{:,}'.format(value)


@register.filter(name='show_jalali_date')
def show_jalali_date(value):
    return date2jalali(value)