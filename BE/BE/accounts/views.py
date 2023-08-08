from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import Teacher, Student
from .serializers import (
    TeacherSignUpSerializer,
    StudentSignUpSerializer,
    TeacherLoginSerializer,
    StudentLoginSerializer,
)

# Create your views here.
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect
import urllib


# 답변자 ViewSet
class TeacherSignUpView(APIView):
    permission_classes = [AllowAny]  # 모든 사용자 접근가능(인증 없어도-Token없이 하는 방법인것 같아서 씀)

    # 답변자 회원가입
    def post(self, request):
        serializer = TeacherSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입 성공"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 회원정보조회
    def get(self, request):
        teachers = Teacher.objects.all()  # 모든 답변자 정보 조회
        serializer = TeacherSignUpSerializer(
            teachers, many=True
        )  # 여러 객체를 직렬화할 때는 many=True 옵션 사용
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentSignUpView(APIView):
    permission_classes = [AllowAny]

    # 질문자 회원가입
    def post(self, request):
        serializer = StudentSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입 성공"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 회원정보조회
    def get(self, request):
        students = Student.objects.all()  # 모든 질문자 정보 조회
        serializer = StudentSignUpSerializer(
            students, many=True
        )  # 여러 객체를 직렬화할 때는 many=True 옵션 사용
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeacherLoginView(APIView):
    def post(self, request):
        serializer = TeacherLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)  # 로그인 처리
                return Response({"message": "로그인 성공"}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"message": "이메일 또는 비밀번호가 올바르지 않습니다."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentLoginView(APIView):
    def post(self, request):
        serializer = StudentLoginSerializer(data=request.data)
        if serializer.is_valid():
            student_id = serializer.validated_data["id"]
            phone = serializer.validated_data["phone"]

            # Student 모델에서 학생 찾기
            try:
                student = Student.objects.get(id=student_id, phone=phone)
                # 필요한 추가 작업 수행
                return Response({"message": "로그인 성공"}, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response(
                    {"message": "학생 정보가 일치하지 않습니다."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        # 사용자 로그아웃 처리
        logout(request)
        return Response({"message": "로그아웃 되었습니다."}, status=status.HTTP_200_OK)


# code 요청
def kakao_login(request):
<<<<<<< HEAD
    app_rest_api_key = "942c23a0e6d71ed610295448ee869edc"
    redirect_uri = "http://127.0.0.1:8000/account/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )


# access token 요청
def kakao_callback(request):
    params = urllib.parse.urlencode(request.GET)
    return redirect(f"http://127.0.0.1:8000/account/login/kakao/callback?{params}")
=======
    app_rest_api_key = '942c23a0e6d71ed610295448ee869edc'
    redirect_uri = "http://127.0.0.1:8000/kakao/callback"
    redirect_url = "https://kauth.kakao.com/oauth/authorize?client_id=" + app_rest_api_key + "&redirect_uri=" + redirect_uri + "&response_type=code"
    return redirect(redirect_url)
    # return redirect(
    #     f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    # )


# access token 요청
def kakao_callback(request):                                                                  
    params = urllib.parse.urlencode(request.GET)
    redirect_url = 'http://127.0.0.1:8000/kakao/callback?' + params
    main_home_url = "http://127.0.0.1:8000"
    return redirect(main_home_url)
    # return redirect(redirect_url)                                
    # return redirect(f'http://127.0.0.1:8000/kakao/callback?{params}')
>>>>>>> back
