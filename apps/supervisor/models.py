from django.db import models


class SupervisorProfile(models.Model):
    class Meta:
        app_label = "apps"

    user = models.OneToOneField("apps.User", on_delete=models.CASCADE)
    institution = models.ForeignKey("apps.InstitutionProfile", on_delete=models.CASCADE)
    department = models.CharField(max_length=50)
