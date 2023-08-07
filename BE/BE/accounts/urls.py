from django.urls import path, include
from . import views
from rest_framework import urls
from .views import kakao_callback, kakao_login

urlpatterns =[
    path('api-auth/', include('rest_framework.urls')),

    # 소셜 로그인
    path('account/login/kakao/', kakao_login, name='kakao_login'),
    path('account/login/kakao/callback/', kakao_callback, name='kakao_callback'),
]