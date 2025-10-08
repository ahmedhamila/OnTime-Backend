from datetime import date

from rest_framework.exceptions import APIException
from rest_framework.exceptions import ValidationError

from src.employees.models.ClockRecord import ClockRecord
from src.employees.models.Employee import Employee
from src.employees.models.EmployeeScore import EmployeeScore


class ClockService:
    @staticmethod
    def create_clock_record(request):
        try:
            data = request.data
            files = request.FILES
            pin_code = data.get("pin_code")
            clock_type = data.get("clock_type")
            lat = data.get("location_lat")
            lng = data.get("location_lng")
            photo = files.get("photo")

            # Validate employee
            try:
                employee = Employee.objects.get(pin_code=pin_code)
            except Employee.DoesNotExist:
                raise ValidationError("Code PIN invalide.")

            # Enforce 1 clock-in and 1 clock-out per day
            if ClockRecord.objects.filter(
                employee=employee,
                clock_type=clock_type,
                timestamp__date=date.today(),
            ).exists():
                raise ValidationError(f"L'employé a déjà pointé {clock_type} aujourd'hui.")
            # Prevent clock-out if no clock-in today
            if clock_type == "out":
                if not ClockRecord.objects.filter(
                    employee=employee,
                    clock_type="in",
                    timestamp__date=date.today(),
                ).exists():
                    raise ValidationError(
                        "Impossible de pointer la sortie sans avoir pointé l'entrée aujourd'hui."
                    )
            # Create record
            clock = ClockRecord.objects.create(
                employee=employee,
                clock_type=clock_type,
                location_lat=lat,
                location_lng=lng,
                photo=photo,
            )

            if clock_type == "out":
                EmployeeScore.objects.get_or_create(employee=employee, date=date.today())

            return clock

        except ValidationError:
            raise
        except Exception as e:
            raise APIException(str(e))

    @staticmethod
    def get_employee_by_pin(pin_code):
        try:
            if not pin_code or len(pin_code) != 4:
                raise ValidationError("Le code PIN doit contenir 4 chiffres.")

            try:
                return Employee.objects.get(pin_code=pin_code)
            except Employee.DoesNotExist:
                raise ValidationError("Code PIN invalide. Employé introuvable.")

        except ValidationError:
            raise
        except Exception as e:
            raise APIException(str(e))
