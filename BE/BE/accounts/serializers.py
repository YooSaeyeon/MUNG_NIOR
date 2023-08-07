from rest_framework import serializers
from .models import Teacher, Student

class TeacherSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'password', 'email', 'phone']

class StudentSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'phone']
