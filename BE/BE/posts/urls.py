from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import QuestionViewSet, AnswerViewSet
from rest_framework.routers import DefaultRouter
from .views import MyQuestionsListView, MyAnswersListView

questions_router = DefaultRouter()
questions_router.register("questions", QuestionViewSet, basename="questions")

answer_router = SimpleRouter(trailing_slash=True)
answer_router.register("answers", AnswerViewSet, basename="answer")

urlpatterns = [
    path("", include(questions_router.urls)),
    path("questions/<int:question_id>/", include(answer_router.urls)),
    path("my_questions/", MyQuestionsListView.as_view(), name="my-questions"),
    path("my_answers/", MyAnswersListView.as_view(), name="my-answers"),
]
