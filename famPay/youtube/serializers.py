from rest_framework import serializers
from .models import video, thumbnailURL


class videoSerializer(serializers.ModelSerializer):
    class Meta:
        model = video
        fields = ["title", "description", "publishing_time"]


class thumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = thumbnailURL
        fields = ["video", "url"]
