from rest_framework import serializers
from apps.mentors.models import CompanyMentors


class CompanyMentorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = CompanyMentors
