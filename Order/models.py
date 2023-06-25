from django.db import models
from Authentication.models import CustomUser


class Order(models.Model):
    BUSY = "busy"
    OVERTIME = "overtime"
    DONE = "done"
    REFUSER = "refuse"
    WAITING = "waiting"

    STATUS_CHOICE = (
        (BUSY, "Доставка"),
        (OVERTIME, "Просрочен"),
        (DONE, "Доставлен"),
        (REFUSER, "Отказ"),
        (WAITING, "Отложен"),
    )

    courier = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name="orders", verbose_name="курьеры")

    price = models.IntegerField(verbose_name="цена заказа")
    payment = models.IntegerField(verbose_name="стоимость заказа для курьера")
    weight = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="вес")
    duration = models.DurationField(verbose_name="продолжительность заказа")
    road = models.FloatField(verbose_name="кол-во километров")
    composition = models.TextField(verbose_name="состав заказа")
    status = models.CharField(choices=STATUS_CHOICE, max_length=30, blank=True, null=True, verbose_name="статус заказа")

    order_time = models.DateTimeField(verbose_name="время заказа")

    start_address = models.TextField(verbose_name="начальный адрес")
    start_latitude = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="начальный широта")
    start_longitude = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="начальный долгота")

    end_address = models.TextField(verbose_name="конечный адрес")
    end_latitude = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="конечный широта")
    end_longitude = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="конечный долгота")
