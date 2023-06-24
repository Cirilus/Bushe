from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import DestroyModelMixin, \
    ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin, CreateModelMixin
from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import CustomUser
from .serializers import UserSerializer


@extend_schema_view(
    retrieve=extend_schema(
        tags=['auth'],
        summary="return user by id",
    ),
    list=extend_schema(
        tags=['auth'],
        summary="return all users"
    ),
    destroy=extend_schema(
        tags=['auth'],
        summary="delete the user",
    ),
    partial_update=extend_schema(
        tags=['auth'],
        summary="update the user"
    ),
    create=extend_schema(
        tags=['auth'],
        summary="create the user",
    ),
)
class UserViews(GenericViewSet,
                RetrieveModelMixin,
                CreateModelMixin,
                ListModelMixin,
                UpdateModelMixin,
                DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = CustomUser
    http_method_names = ["patch", "get", "delete", "post"]

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(self.queryset, id=pk)

    def get_queryset(self):
        return self.queryset.objects.all()
