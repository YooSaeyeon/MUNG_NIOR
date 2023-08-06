from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework.viewsets import ModelViewSet


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(writer = self.request.user)


# 18번줄 헷갈리는 코드
class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        serializer.save(writer = self.request.user)

    def get_queryset(self, **kwargs): # Override
        id = self.kwargs['question_id']
        return self.queryset.filter(question=id)