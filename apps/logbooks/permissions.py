from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStudentOrSuervisor(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        match user.role:
            case "student":
                return True
            case "supervisor":
                return request.method in SAFE_METHODS
            case _:
                return False
