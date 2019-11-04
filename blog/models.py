from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)  # 제목 표시 글자수 제한 30글자
    content = MarkdownxField()
    created = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=True)

    def __str__(self):
        return '{} :: {}'.format(self.title, self.author)

    def get_absolute_url(self):
        return '/blog/{}'.format(self.pk)

    def get_markdown_content(self):
        return markdown(self.content)
