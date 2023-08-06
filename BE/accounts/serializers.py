from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework import serializers

CustomUser = get_user_model()

# 답변자 회원가입
class TeacherUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            email = validated_data['email'],
            phoneNumber = validated_data['phoneNumber']
        )
        return user
    
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'phoneNumber' ]


# 질문자 회원가입
class StudentUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username = validated_data['username'],
            phoneNumber = validated_data['phoneNumber']
        )
        return user
    
    class Meta:
        model = CustomUser
        fields = ['username', 'phoneNumber' ]


# 답변자 로그인
class TeacherLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_teacher:
            return user
        raise serializers.ValidationError("유효하지 않은 자격 증명 또는 사용자가 답변자가 아닙니다.")


# 질문자 로그인
class StudentLoginSerializer(serializers.Serializer):
    id = serializers.CharField()
    phoneNumber = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_student:
            return user
        raise serializers.ValidationError("유효하지 않은 자격 증명 또는 사용자가 질문자가 아닙니다.")