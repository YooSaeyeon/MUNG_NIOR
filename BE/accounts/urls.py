from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns =[
    path('teacher/signup/', views.TeacherUserCreate.as_view()),
    path('student/signup/', views.StudentUserCreate.as_view()),
    path('teacher/login/', views.TeacherLoginView.as_view()),  # 선생님 로그인
    path('student/login/', views.StudentLoginView.as_view()),  # 학생 로그인
    path('logout/', views.LogoutView.as_view()),  # 로그아웃
]

# 현재 로그인 부분 링크가 오류남
# 로그인에서 답변자는 email, password / 질문자는 id, phoneNumber만 입력받도록 구현