from apps.supervisors.models import SupervisorProfile
from django.db.models.aggregates import Count
from django.db import models


def assign_supervisor(student):
    supervisors = (
        SupervisorProfile.objects.filter(
            is_verified=True,
            department=student.department,
            institution=student.institution,
        )
        .annotate(student_count=Count("studentplacement"))
        .filter(student_count__lt=models.F("max_students"))
        .order_by("student_count")
    )

    return supervisors.first()
