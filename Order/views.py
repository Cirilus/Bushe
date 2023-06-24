from django.db.models import Count, Avg
from django.db.models.functions import TruncDate
from django.http import HttpResponse
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import DestroyModelMixin, \
    ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin, CreateModelMixin
from django.shortcuts import get_object_or_404, get_list_or_404, render
import pandas as pd

from .models import Order
from .serializers import OrderSerializer


@extend_schema_view(
    retrieve=extend_schema(
        tags=['order'],
        summary="return user by id",
    ),
    list=extend_schema(
        tags=['order'],
        summary="return all users"
    ),
    destroy=extend_schema(
        tags=['order'],
        summary="delete the user",
    ),
    partial_update=extend_schema(
        tags=['order'],
        summary="update the user"
    ),
    create=extend_schema(
        tags=['order'],
        summary="create the user",
    ),
)
class OrderViews(GenericViewSet,
                 RetrieveModelMixin,
                 CreateModelMixin,
                 ListModelMixin,
                 UpdateModelMixin,
                 DestroyModelMixin):
    serializer_class = OrderSerializer
    queryset = Order
    http_method_names = ["patch", "get", "delete", "post"]

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(self.queryset, id=pk)

    def get_queryset(self):
        return self.queryset.objects.all()


class ReportUploadView(GenericViewSet):
    queryset = Order
    serializer_class = OrderSerializer

    @extend_schema(
        tags=["csv"],
        summary="upload the report"
    )
    def get(self, request):
        orders = self.queryset.objects.all()
        orders = self.serializer_class(orders, many=True).data
        df = pd.DataFrame(orders)
        csv = df.to_csv()
        response = HttpResponse(csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="orders.csv"'

        return response
        # return Response(status=201)


class OrderStatistic(GenericViewSet):
    queryset = Order

    @extend_schema(
        tags=["statistic"],
        summary="the count of all orders"
    )
    def get(self, request):
        return Response(status=201, data={"counts": self.queryset.objects.count()})


class StatusStatistic(GenericViewSet):
    queryset = Order

    @extend_schema(
        tags=["statistic"],
        summary="the counts of the statues"
    )
    def get(self, request):
        return Response(status=201, data=self.queryset.objects.values('status').annotate(
            count=Count("pk")
        ).order_by("count"))


class AverageBillStatistic(GenericViewSet):
    queryset = Order

    @extend_schema(
        tags=["statistic"],
        summary="the average bill"
    )
    def get(self, request):
        return Response(status=201, data=self.queryset.objects.annotate(avg_price=Avg("price")))


class AverageDailyBillStatistic(GenericViewSet):
    queryset = Order

    @extend_schema(
        tags=["statistic"],
        summary="the average daily bill"
    )
    def get(self, request):
        averages = self.queryset.objects.annotate(
            date=TruncDate("order_time")).values("date").annotate(average_price=Avg("price")).order_by("date")
        return Response(status=201, data=averages)
