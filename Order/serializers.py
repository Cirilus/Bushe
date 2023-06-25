from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Order, Location, Composition
from drf_writable_nested import WritableNestedModelSerializer


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ("latitude", "longitude", "address",)


class CompositionSerializer(ModelSerializer):
    class Meta:
        model = Composition
        fields =("title", "price", "weight", "count",)


class OrderSerializer(WritableNestedModelSerializer):
    courier = SerializerMethodField()
    composition = CompositionSerializer(many=True)
    location = LocationSerializer(many=True)

    def get_courier(self, instance):
        if instance.courier:
            return instance.courier.firstname + " " + instance.courier.lastname
        return None

    class Meta:
        model = Order
        fields = ("id", "price", "courier", "payment", "weight", "road",
                  "duration", "composition", "order_time",
                  "status", "location",)

