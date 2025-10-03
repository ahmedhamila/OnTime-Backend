from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from src.employees.models.Employee import Employee
from src.employees.serializers.EmployeeSerializer import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
