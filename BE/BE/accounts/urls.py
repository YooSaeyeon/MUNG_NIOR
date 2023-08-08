from django.urls import path, include
from django.urls import path
from .views import (
    TeacherSignUpView,
    StudentSignUpView,
    TeacherLoginView,
    StudentLoginView,
    LogoutView,
)
from .views import kakao_callback, kakao_login

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("teacher/signup/", TeacherSignUpView.as_view(), name="teacher-signup"),
    path("student/signup/", StudentSignUpView.as_view(), name="student-signup"),
    path("teacher/login/", TeacherLoginView.as_view(), name="teacher-login"),
    path("student/login/", StudentLoginView.as_view(), name="student-login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # 소셜 로그인
    path("kakao/", kakao_login, name="kakao_login"),
    path("kakao/callback/", kakao_callback, name="kakao_callback"),
]
