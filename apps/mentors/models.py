from django.db import models
import uuid


class CompanyMentor(models.Model):
    class Meta:
        app_label = "apps"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey("apps.Company", on_delete=models.CASCADE)
    user = models.OneToOneField("apps.User", on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    institutions_that_verified = models.ManyToManyField(
        "apps.InstitutionProfile",
        null=True,
        blank=True,
        related_name="verified_mentors",
    )
    max_students = models.IntegerField(default=20)


class MentorInvitation(models.Model):
    class Meta:
        app_label = "apps"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    company = models.ForeignKey("apps.Company", on_delete=models.CASCADE)
    role = models.CharField(dafault="mentor")
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
