from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from src.employees.models.Employee import Employee
from src.employees.serializers.EmployeeSerializer import EmployeeSerializer
from src.employees.services.EmployeeService import EmployeeService


class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ["get_by_pin"]:
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=["post"], url_path="by-pin")
    def get_by_pin(self, request):
        pin_code = request.data.get("pin_code")

        employee = EmployeeService.get_employee_by_pin(pin_code)
        serializer = self.get_serializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
