from django.contrib.auth.backends import BaseBackend
from .models import Admin_User


class CustomEmployeeAuthenticationBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            employee = Admin_User.objects.get(email=email)
            print(employee)
        except Admin_User.DoesNotExist:
            return None

        if employee.check_password(password):
            print(employee.check_password(password))
            return employee

        return None

    def get_user(self, user_id):
        try:
            return Admin_User.objects.get(pk=user_id)
        except Admin_User.DoesNotExist:
            return None
