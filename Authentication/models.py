from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from Authentication.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    MANAGER = "manager"
    DELIVER = "deliver"
    SUPPORT = "support"
    CUSTOMER = "customer"

    ROLE_CHOICE = (
        (MANAGER, "Менеджер"),
        (DELIVER, "Курьер"),
        (SUPPORT, "Поддержка"),
        (CUSTOMER, "Клиент"),
    )

    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone = models.TextField(unique=True, verbose_name="Телефон")

    firstname = models.CharField(max_length=30, verbose_name='Имя')
    lastname = models.CharField(max_length=30, verbose_name='Фамилия')

    role = models.CharField(choices=ROLE_CHOICE, max_length=30, blank=True, null=True, verbose_name="роль")

    bonus_balance = models.IntegerField(null=True, blank=True, verbose_name="бонусный баланс")
    balance = models.IntegerField(null=True, blank=True, verbose_name="баланс")

    rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="рейтинг", default=0.0)

    is_active = models.BooleanField(default=False, verbose_name='Активированный аккаунт')
    is_staff = models.BooleanField(default=False, verbose_name="Админ")

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

