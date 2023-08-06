from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from .serializers import TeacherUserSerializer, StudentUserSerializer, TeacherLoginSerializer, StudentLoginSerializer
from .models import CustomUser
from rest_framework import generics

from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

CustomUser = get_user_model()

# 회원가입
class TeacherUserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = TeacherUserSerializer

class StudentUserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = StudentUserSerializer


# 답변자 로그인
class TeacherLoginView(APIView):
    def post(self, request):
        serializer = TeacherLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            auth_login(request, user)
            return JsonResponse({"message": "선생님이 성공적으로 로그인되었습니다."})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 질문자 로그인
class StudentLoginView(APIView):
    def post(self, request):
        serializer = StudentLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            auth_login(request, user)
            return JsonResponse({"message": "학생이 성공적으로 로그인되었습니다."})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 로그아웃
class LogoutView(APIView):
    def post(self, request):
        auth_logout(request)
        return JsonResponse({"message": "성공적으로 로그아웃되었습니다."})
