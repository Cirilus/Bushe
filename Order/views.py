from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import DestroyModelMixin, \
    ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin, CreateModelMixin
from django.shortcuts import get_object_or_404, get_list_or_404, render

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
