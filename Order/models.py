from django.db import models
from Authentication.models import CustomUser


class Location(models.Model):
    latitude = models.FloatField(verbose_name="широта")
    longitude = models.FloatField(verbose_name="долгота")
    address = models.TextField(verbose_name="адрес")


class Composition(models.Model):
    title = models.TextField(verbose_name="название")
    price = models.IntegerField(verbose_name="цена")
    weight = models.FloatField(verbose_name="вес")
    count = models.IntegerField(verbose_name="количество")


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
    weight = models.FloatField(verbose_name="вес")
    duration = models.DurationField(verbose_name="продолжительность заказа")
    road = models.FloatField(verbose_name="кол-во километров")

    composition = models.ManyToManyField(Composition, related_name="order", verbose_name="Пути доставки")

    status = models.CharField(choices=STATUS_CHOICE, max_length=30, blank=True, null=True, verbose_name="статус заказа")

    order_time = models.DateTimeField(verbose_name="время заказа")

    location = models.ManyToManyField(Location, related_name="order", verbose_name="Пути доставки")






