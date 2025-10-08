from datetime import date

from django.db import models

from src.employees.models.Employee import Employee
from src.utils.models.BaseModel import BaseModel


class EmployeeScore(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="scores")
    date = models.DateField(default=date.today)

    class Meta:
        unique_together = ("employee", "date")
        indexes = [models.Index(fields=["employee", "date"])]

    def __str__(self):
        return f"{self.employee} - {self.date}"
