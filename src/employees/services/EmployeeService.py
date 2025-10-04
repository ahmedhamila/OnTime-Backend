from rest_framework.exceptions import APIException
from rest_framework.exceptions import ValidationError

from src.employees.models.Employee import Employee


class EmployeeService:
    @staticmethod
    def get_employee_by_pin(pin_code: str):
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
