from datetime import date

from rest_framework import serializers

from src.employees.models.Employee import Employee
from src.employees.models.EmployeeScore import EmployeeScore


class EmployeeSerializer(serializers.ModelSerializer):
    monthly_score = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ["id", "first_name", "last_name", "phone_number", "pin_code", "monthly_score"]
        read_only_fields = ["id"]

    def get_monthly_score(self, obj):
        today = date.today()
        return EmployeeScore.objects.filter(
            employee=obj,
            date__year=today.year,
            date__month=today.month,
        ).count()
