from django.db import models
import uuid


class SupervisorProfile(models.Model):
    class Meta:
        app_label = "apps"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField("apps.User", on_delete=models.CASCADE)
    institution = models.ForeignKey("apps.InstitutionProfile", on_delete=models.CASCADE)
    department = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    max_students = models.IntegerField(default=40)
