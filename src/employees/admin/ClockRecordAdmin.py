from django.contrib import admin

from src.employees.models.ClockRecord import ClockRecord


@admin.register(ClockRecord)
class ClockRecordAdmin(admin.ModelAdmin):
    list_display = ("employee", "clock_type", "timestamp")
    list_filter = ("clock_type", "timestamp")
    search_fields = ("employee__first_name", "employee__last_name", "employee__pin_code")
