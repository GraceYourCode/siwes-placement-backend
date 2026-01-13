import uuid
from django.db import models


class Company(models.Model):
    class Meta:
        app_label = "apps"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300)
    is_verified = models.BooleanField(default=False)
    registration_number = models.CharField(null=True, blank=True)
    registration_document = models.FileField(
        upload_to="company_docs/", blank=True, null=True
    )
    registration_body = models.CharField(blank=True, null=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
