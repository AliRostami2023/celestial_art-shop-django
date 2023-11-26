from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    email_active_code = models.CharField(max_length=200, null=False, blank=True, verbose_name='ایمیل فعالسازی')

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'مشخصات کاربر'
        verbose_name_plural = 'کاربران'
