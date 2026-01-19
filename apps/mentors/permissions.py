from rest_framework.permissions import BasePermission


class IsMentor(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user.role == "mentor":
            return True
        return False
