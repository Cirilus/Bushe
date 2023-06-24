from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViews

router = DefaultRouter()

router.register("", OrderViews, basename="order")


urlpatterns = [
    path("", include(router.urls)),
]