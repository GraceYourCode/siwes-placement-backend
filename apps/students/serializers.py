from rest_framework import serializers
from .models import StudentInstitutionProfile
from apps.students.models import StudentPlacement


class StudentInstitutionProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInstitutionProfile
        fields = "__all__"
        read_only_fields = ["institution", "user"]


class StudentPlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPlacement
        fields = "__all__"
        read_only_fields = ["supervisor"]
