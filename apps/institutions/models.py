import uuid
from django.db import models


class InstitutionProfile(models.Model):
    class Meta:
        app_label = "apps"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    short_code = models.CharField(max_length=20)
    address = models.TextField()

    siwes_duration_months = models.IntegerField(default=4)
    grading_policy = models.CharField(max_length=100)

    def __str__(self):
        return self.name
