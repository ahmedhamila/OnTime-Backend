from django.urls import include
from django.urls import path

from rest_framework import routers

from src.employees.controllers.EmployeeViewSet import EmployeeViewSet


router = routers.DefaultRouter()
router.register("employees", EmployeeViewSet, basename="employee")
urlpatterns = [
    path("", include(router.urls)),
]
