from rest_framework import serializers
from .models import StudentInstitutionProfile


class StudentInstitutionProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInstitutionProfile
        fields = "__all__"
        read_only_fields = ["institution", "user"]
