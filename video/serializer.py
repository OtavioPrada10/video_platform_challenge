from rest_framework import serializers
from video.models import Video

class VideoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=100)
    url = serializers.CharField(max_length=100)