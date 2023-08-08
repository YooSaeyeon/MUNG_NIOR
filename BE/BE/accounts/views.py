from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher, Student
from .serializers import TeacherSignUpSerializer, StudentSignUpSerializer

# Create your views here.
from django.shortcuts import redirect
import urllib

# 답변자 ViewSet
class TeacherSignUpViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSignUpSerializer

class StudentSignUpViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSignUpSerializer

# code 요청
def kakao_login(request):
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