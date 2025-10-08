from django.contrib import admin

from src.employees.models.EmployeeScore import EmployeeScore


@admin.register(EmployeeScore)
class EmployeeScoreAdmin(admin.ModelAdmin):
    list_display = ("employee", "date", "created_at")
    list_filter = ("date",)
    search_fields = ("employee__first_name", "employee__last_name", "employee__pin_code")
    ordering = ("-date",)
