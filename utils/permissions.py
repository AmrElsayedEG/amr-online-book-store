from rest_framework.permissions import BasePermission
from .choices import UserTypeChoices

class IsCustomer(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.user_type == UserTypeChoices.CUSTOMER)