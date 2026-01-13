from rest_framework import serializers
from .models import LogbookEntry, Reviews, Logbook


class LogbookEntrySerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField

    class Meta:
        model = LogbookEntry
        fields = "__all__"
        read_only_fields = ["timestamp", "status", "placement", "logbook", "reviews"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"


class LogbookSerializer(serializers.ModelSerializer):
    entries = serializers.SerializerMethodField

    class Meta:
        model = Logbook
        fields = "__all__"
        read_only_fields = ["id", "student"]
