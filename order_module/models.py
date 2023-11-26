from django.db import models

from account_module.models import User
from product_module.models import Product


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='نهایی شده/نشده')
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')
    postal_tracking_code = models.CharField(max_length=80, null=True, blank=True, verbose_name='کد رهگیری پستی')

    def __str__(self):
        return self.user.email

    def calculate_total_price(self):
        total_amount = 0
        if self.is_paid:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.final_price * order_detail.count
        else:
            for order_detail in self.orderdetail_set.all():
                if order_detail.product.price2:
                    total_amount += order_detail.product.price2 * order_detail.count
                else:
                    total_amount += order_detail.product.price1 * order_detail.count

        return total_amount

    class Meta:
        verbose_name = 'سفارشات کاربر'
        verbose_name_plural = 'لیست سفارشات کاربران'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def get_total_price(self):
        if self.product.price2:
            return self.count * self.product.price2
        else:
            return self.count * self.product.price1

    def __str__(self):
        return self.order.user.email

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'لیست جزییات سبدهای خرید'


class OrderCheckout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='فاکتور')
    first_name = models.CharField(max_length=150, verbose_name='نام')
    last_name = models.CharField(max_length=150, verbose_name='نام خانوادگی')
    state = models.CharField(max_length=80, verbose_name='استان')
    city = models.CharField(max_length=80, verbose_name='شهر')
    zipcode = models.CharField(max_length=30, verbose_name='کد پستی')
    phone = models.CharField(max_length=12, verbose_name='شماره تماس')
    address = models.TextField(max_length=1500, verbose_name='آدرس کامل')
    sended = models.BooleanField(default=False, verbose_name='ارسال شده / نشده')

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'مشخصات کاربر'
        verbose_name_plural = 'لیست مشخصات کاربران'

