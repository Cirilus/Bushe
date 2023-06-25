from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Order


class OrderSerializer(ModelSerializer):
    courier = SerializerMethodField()

    def get_courier(self, instance):
        if instance.courier:
            return instance.courier.firstname + " " + instance.courier.lastname
        return None

    class Meta:
        model = Order
        fields = ("id", "price", "courier", "payment", "weight", "road", "duration", "composition", "order_time",
                  "status", "start_address", "start_latitude", "start_longitude",
                  "end_address", "end_latitude", "end_longitude",)

