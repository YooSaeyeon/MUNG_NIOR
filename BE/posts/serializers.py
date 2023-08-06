from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Question, Answer
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class QuestionSerializer(ModelSerializer):
    writer = serializers.ReadOnlyField(source = 'writer.username')

    class Meta:
        model = Question
        fields = [ 'content', 'writer' ]

class AnswerSerializer(ModelSerializer):
    writer = serializers.ReadOnlyField(source = 'writer.username')

    class Meta:
        model = Answer
        fields = [ 'comment', 'question', 'photo', 'writer' ]