from rest_framework import serializers
from apps.supervisors.models import SupervisorProfile


class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = SupervisorProfile
        read_only_fields = ["is_verified, id", "max_students", "user", "institution"]
