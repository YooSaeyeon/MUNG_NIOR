from django.db import models

# 전화번호 010-0000-0000 형식으로 하기로 함
# 답변자
class Teacher(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13) 

    def __str__(self):
        return self.id
    
# 질문자
class Student(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    phone = models.CharField(max_length=13)  

    def __str__(self):
        return self.id
    