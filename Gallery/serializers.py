from rest_framework import serializers
from .models import Room, Image


class RoomListSerializer(serializers.ModelSerializer):
    api_url = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ['title', 'slug', 'api_url']

    def get_api_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.get_api_url())


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["image", "caption"]


class RoomSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ["title", "slug", "images"]
