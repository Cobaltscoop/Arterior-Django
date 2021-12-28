from django.db.models import fields
from rest_framework  import serializers
from .models import Artist, Assistant, Gallery, Store


class ArtistSerializer(serializers.ModelSerializer):

    def validate(self, data):
        return super().validate(data)

    class Meta:
        model = Artist
        fields = "__all__"


class AssistantSerializer(serializers.ModelSerializer):

    def validate(self, data):
        return super().validate(data)

    class Meta:
        model = Assistant
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):

    def validate(self, data):
        return super().validate(data)

    class Meta:
        model = Gallery
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):

    def validate(self, data):
        return super().validate(data)

    class Meta:
        model = Store
        fields = "__all__"