from django.db import models
from django.contrib.auth.models import User


class Vacancy(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_data = models.DateTimeField()
