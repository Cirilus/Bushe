from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViews, StatusStatistic, OrderStatistic, \
    AverageBillStatistic, AverageDailyBillStatistic, ReportUploadView

router = DefaultRouter()

router.register("", OrderViews, basename="order")


urlpatterns = [
    path("statistic/orders/", OrderStatistic.as_view({"get": "get"}), name="statistic-courier"),
    path("statistic/status/", StatusStatistic.as_view({"get": "get"}), name="statistic-status"),
    path("statistic/avg_bill/", AverageBillStatistic.as_view({"get": "get"}), name="avg-status"),
    path("statistic/avg_daily_bill/", AverageDailyBillStatistic.as_view({"get": "get"}), name="avg-daily-status"),
    path("csv/", ReportUploadView.as_view({"get": "get"}), name="upload csv"),
    path("", include(router.urls)),
]
