from django.shortcuts import render

# Create your views here.
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework.viewsets import ModelViewSet

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# 질문자
class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(writer = self.request.user)


# 답변자
class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        serializer.save(writer = self.request.user)

    def get_queryset(self, **kwargs): # Override
        id = self.kwargs['question_id']
        return self.queryset.filter(question=id)
    


# 질문자 마이페이지
class MyQuestionsListView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Question.objects.filter(writer=user)
    

# 답변자 마이페이지
class MyAnswersListView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Answer.objects.filter(writer=user)