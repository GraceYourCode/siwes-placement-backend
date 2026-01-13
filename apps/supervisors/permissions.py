from rest_framework.permissions import BasePermission


class IsSupervisor(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user.role == "supervisor":
            return True
        return False
