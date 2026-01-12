from rest_framework.permissions import BasePermission


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user.role == "student":
            return True
        return False
