import uuid
from django.db import models


class CompanyProfile(models.Model):
    class Meta:
        app_label = "apps"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField("apps.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    short_code = models.CharField(max_length=20)
    address = models.TextField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name
