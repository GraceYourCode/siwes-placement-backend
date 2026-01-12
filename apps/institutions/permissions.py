from rest_framework.permissions import BasePermission


class IsInstitution(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user.role == "institution":
            return True
        return False
