import uuid
from django.db import models
from apps.students.utils import placement_letter_upload_path


class StudentInstitutionProfile(models.Model):
    class Meta:
        app_label = "apps"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField("apps.User", on_delete=models.CASCADE)

    institution = models.ForeignKey("apps.InstitutionProfile", on_delete=models.CASCADE)
    matric_no = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50, null=True, blank=True)
    programme = models.CharField(max_length=50)
    level = models.CharField(max_length=20)

    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("active", "Active"),
            ("completed", "Completed"),
        ],
        default="pending",
    )

    def __str__(self):
        return self.matric_no


class StudentPlacement(models.Model):
    class Meta:
        app_label = "apps"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(StudentInstitutionProfile, on_delete=models.CASCADE)

    company = models.ForeignKey("apps.Company", on_delete=models.CASCADE)
    placement_status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("verified", "Verified"),
            ("rejected", "Rejected"),
        ],
        default="pending",
    )
    placement_letter = models.FileField(
        upload_to=placement_letter_upload_path, null=True, blank=True
    )
    is_active = models.BooleanField(default=False)

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    supervisor = models.ForeignKey(
        "apps.SupervisorProfile", null=True, blank=True, on_delete=models.SET_NULL
    )

    mentor = models.ForeignKey(
        "apps.CompanyMentor", null=True, blank=True, on_delete=models.SET_NULL
    )
