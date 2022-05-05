from rest_framework import serializers

from .models import Language


class LanguageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = (
            'id',
            'language',
            'piston_lang',
            'editor_lang',
        )


class LanguageDemoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = (
            'demo_code',
        )