from rest_framework import serializers

from src.employees.models.Employee import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "first_name", "last_name", "phone_number", "pin_code"]
        read_only_fields = ["id"]
