from rest_framework.permissions import BasePermission
from apps.students.models import StudentPlacement


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user.role == "student":
            return True
        return False


class IsPlacementValid(BasePermission):
    def has_permission(self, request, view):
        student = request.user.studentinstitutionprofile
        print("omo eba cold gan oo", student)

        return StudentPlacement.objects.filter(student=student, is_active=True).exists()
