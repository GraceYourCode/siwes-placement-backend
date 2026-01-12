from rest_framework import serializers
from apps.institutions.models import InstitutionProfile


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutionProfile
        fields = "__all__"
        read_only_fields = ["user"]
