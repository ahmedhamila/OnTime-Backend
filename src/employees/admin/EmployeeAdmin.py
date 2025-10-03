from django.contrib import admin

from src.employees.models.Employee import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone_number", "pin_code"]
    search_fields = ["first_name", "last_name", "phone_number"]
