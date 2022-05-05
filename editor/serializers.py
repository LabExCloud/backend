from rest_framework import serializers

from .models import Language, Question


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


class QuestionSerializer(serializers.ModelSerializer):
    language = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all())
    class Meta:
        model = Question
        fields = (
            'id',
            'question_number',
            'question',
            'language',
            'answer',
            'mark',
            'fullscreen',
        )