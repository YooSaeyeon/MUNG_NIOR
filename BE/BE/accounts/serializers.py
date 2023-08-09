from rest_framework import serializers
from .models import Teacher, Student


class TeacherSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "password", "email", "phone"]


class TeacherLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)


class StudentSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "phone"]


class StudentLoginSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=50, write_only=True)
    phone = serializers.CharField(max_length=13)
