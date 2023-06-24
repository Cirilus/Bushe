from rest_framework.serializers import ModelSerializer
from .models import Order


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("price", "payment", "weight", "duration", "composition", "order_time",
                  "status", "start_address", "start_latitude", "start_longitude",
                  "end_address", "end_latitude", "end_longitude",)

