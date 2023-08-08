from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherSignUpViewSet, StudentSignUpViewSet
from .views import kakao_callback, kakao_login

router = DefaultRouter()
router.register(r'teacher/signup', TeacherSignUpViewSet, basename='teacher-signup')
router.register(r'student/signup', StudentSignUpViewSet, basename='student-signup')


urlpatterns =[
    path('api-auth/', include('rest_framework.urls')),

    path('', include(router.urls)), # teacher url
    path('student/signup/', include(router.urls)), 

    # 소셜 로그인
    path('kakao/', kakao_login, name='kakao_login'),
    path('kakao/callback/', kakao_callback, name='kakao_callback'),
]