from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


# Create your models here.
# 질문자 model
class Question(models.Model):
    content = models.TextField()
    created_at = models.DateField(verbose_name="작성일", auto_now_add=True)
    writer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content
    
# 답변자 model
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateField(verbose_name="작성일", auto_now_add=True)
    photo = models.ImageField(verbose_name="이미지", blank=True, null=True)
    writer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.comment