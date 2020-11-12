from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


# class MyUser(User):
#     employer = models.BooleanField()

class Worker(models.Model):
    age = models.DateField(null=True)
    first_name = models.CharField(max_length=32)
    second_name = models.CharField(max_length=32)
    education = models.TextField(max_length=64)
    work_experience = models.TextField(max_length=1024)
    country = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    e_mail = models.EmailField()
    phone = models.IntegerField(null=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE)


class Employer(models.Model):
    age = models.DateField()
    name = models.CharField(max_length=32)
    number_vacancy = models.IntegerField()
    country = models.CharField(max_length=32)
    city = models.TextField(max_length=32)
    phone = models.IntegerField()
    e_mail = models.EmailField()
    sphere = models.CharField(max_length=32)
    account = models.ForeignKey(User, on_delete=models.CASCADE) # должен быть либо админ, либо спец аккаунт
