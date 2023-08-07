from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Question, Answer
# from accounts.models import User


class QuestionSerializer(ModelSerializer):
    # writer = serializers.ReadOnlyField(source = 'writer.username')

    class Meta:
        model = Question
        fields = [ 'content']
        # fields = [ 'content', 'writer' ]

class AnswerSerializer(ModelSerializer):
    # writer = serializers.ReadOnlyField(source = 'writer.username')

    class Meta:
        model = Answer
        fields = [ 'comment', 'question', 'photo']
        # fields = [ 'comment', 'question', 'photo', 'writer' ]