from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    is_public = serializers.BooleanField(required=True)
    photos = serializers.ListSerializer(child=serializers.CharField(), write_only=True)

    class Meta:
        model = Note
        fields = [
            'id',
            'user',
            'title',
            'is_public',
            'text',
            'created_at',
            'photos',
        ]
        read_only_fields = ['user']

    def validate_is_public(self, value):
        if value:
            user = self.context['request'].user
            if Note.objects.filter(user=user, is_public=False).count() > 5:
                raise ValidationError('too many private notes')
        return value

    def validate_photos(self, value):
        if value:
            if len(value) < 3:
                raise ValidationError('error!')
        return value

    def create(self, validated_data):
        photos = validated_data.pop('photos')
        print(photos)
        return super().create(validated_data)
