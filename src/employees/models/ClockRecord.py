from django.db import models

from src.employees.models.Employee import Employee
from src.utils.models.BaseModel import BaseModel


class ClockRecord(BaseModel):
    CLOCK_TYPES = [
        ("in", "Clock In"),
        ("out", "Clock Out"),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="clock_records")
    clock_type = models.CharField(max_length=3, choices=CLOCK_TYPES)
    location_lat = models.FloatField()
    location_lng = models.FloatField()
    photo = models.ImageField(upload_to="clock_photos/")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("employee", "clock_type", "timestamp")

    def __str__(self):
        return f"{self.employee} - {self.clock_type} @ {self.timestamp}"
