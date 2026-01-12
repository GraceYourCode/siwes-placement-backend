import uuid
from django.db import models


class Logbook(models.Model):
    class Meta:
        app_label = "apps"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.OneToOneField(
        "apps.StudentInstitutionProfile", on_delete=models.CASCADE
    )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.student


class LogbookEntry(models.Model):
    class Meta:
        app_label = "apps"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    logbook = models.ForeignKey(
        Logbook, on_delete=models.CASCADE, related_name="entries"
    )
    placement = models.ForeignKey("apps.StudentPlacement", on_delete=models.CASCADE)
    date = models.DateField()
    activity_summary = models.TextField()
    hours_worked = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("approved", "Approved")],
        default="pending",
    )
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Entry by {self.logbook} on {self.date}"


class Reviews(models.Model):
    class Meta:
        app_label = "apps"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    entry = models.ForeignKey(
        LogbookEntry, on_delete=models.CASCADE, related_name="reviews"
    )
    supervisor = models.ForeignKey("apps.SupervisorProfile", on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.entry} by {self.supervisor}"
