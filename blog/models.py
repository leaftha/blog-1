from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)  # 제목 표시 글자수 제한 30글자
    content = models.TextField(null=True)
    created = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=True)