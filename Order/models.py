from django.db import models
from Authentication.models import CustomUser


class Order(models.Model):
    PROCESSING = 0
    PREPARED = 1
    READY = 2
    DELIVERED = 3
    UNDELIVERED = 4

    STATUS_CHOICE = (
        (PROCESSING, "в обработке"),
        (PREPARED, "готовится"),
        (READY, "готов"),
        (DELIVERED, "доставлен"),
        (UNDELIVERED, "не доставлен"),
    )

    courier = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name="orders", verbose_name="курьеры")

    price = models.IntegerField(verbose_name="цена заказа")
    payment = models.IntegerField(verbose_name="стоимость заказа для курьера")
    weight = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="вес")
    duration = models.DurationField(verbose_name="продолжительность заказа")
    composition = models.TextField(verbose_name="состав заказа")
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICE, blank=True, null=True, verbose_name="статус заказа")

    start_address = models.TextField(verbose_name="начальный адрес")
    start_latitude = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="начальный широта")
    start_longitude = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="начальный долгота")

    end_address = models.TextField(verbose_name="конечный адрес")
    end_latitude = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="конечный широта")
    end_longitude = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="конечный долгота")
