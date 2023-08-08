from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import QuestionViewSet, AnswerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("questions", QuestionViewSet)

answer_router = SimpleRouter(trailing_slash=True)
answer_router.register("answers", AnswerViewSet, basename="answer")

urlpatterns = [
    path("", include(router.urls)),
    path("questions/<int:question_id>/", include(answer_router.urls)),
]
