from rest_framework import serializers

from src.employees.models.ClockRecord import ClockRecord
from src.employees.serializers.EmployeeSerializer import EmployeeSerializer


class ClockRecordSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = ClockRecord
        fields = [
            "id",
            "employee",
            "clock_type",
            "location_lat",
            "location_lng",
            "photo",
            "timestamp",
        ]
        read_only_fields = ["id", "timestamp", "employee"]
