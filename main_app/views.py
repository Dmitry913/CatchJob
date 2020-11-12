from django.views.generic.base import TemplateView


from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, HttpRequest, HttpResponseBadRequest
from .models import Worker, Employer
from resume.models import Resume
from vacancy.models import Vacancy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView


from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


from datetime import datetime

def my_is_staff(my_user):
    return my_user.is_staff


class MainPage(TemplateView):
    template_name = 'main_app/main_page.html'


class HomePage(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if my_is_staff(request.user): # сделать свой класс пользователя, для выдачи работадателям
                return render(request, 'main_app/home_page.html',
                              context={"auth": True, 'employer': True, 'data': Employer.objects.filter(account=request.user), 'vacancy': Vacancy.objects.filter(author=request.user)})
            else:
                return render(request, 'main_app/home_page.html',
                              context={"auth": True, 'employer': False, 'data': Worker.objects.filter(account=request.user), 'resume': Resume.objects.filter(author=request.user)})
        else:
            return render(request, 'main_app/home_page.html', context={'auth': False})

    def post(self, request, *args, **kwargs):
        data = [request.POST.get('description'), request.POST.get('title')]

        if data:
            if my_is_staff(request.user):
                Vacancy(author=request.user)
                Vacancy.objects.create(title=data[1], description=data[0], create_data=datetime.now(), author=request.user)
                return redirect('/vacancy/')
            else:
                try:
                    my_resume = Resume.objects.get(author=request.user)
                except Resume.DoesNotExist:
                    my_resume = Resume(author=request.user)
                my_resume.title = data[1]
                my_resume.description = data[0]
                my_resume.create_data = datetime.now()
                my_resume.save()
                return redirect('/resume/')
        else:
            return HttpResponseBadRequest()

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass


class SignIn(LoginView):
    # redirect_field_name = '/home/'
    template_name = 'main_app/signin.html'


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = '/sign-in/'
    template_name = 'main_app/signup.html'


class LogOut(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect("/")


class UpdateProfile(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'main_app/update_profile.html', context={'employer': True if my_is_staff(request.user) else False})
    # HttpRequest.POST.

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            my_dict = {key: value for key, value in request.POST.dict().items()}
            del my_dict['csrfmiddlewaretoken']
            if my_is_staff(request.user):
                try:
                    my_obj = Employer.objects.get(account=request.user)
                except Employer.DoesNotExist:
                    my_obj = Employer(account=request.user)
                my_obj.name = str(my_dict['name'])
                my_obj.number_vacancy = int(my_dict['number_vacancy'])
                my_obj.sphere = str(my_dict['sphere'])
                my_obj.country = str(my_dict['country'])
                my_obj.city = str(my_dict['city'])
                my_obj.e_mail = str(my_dict['e_mail'])  # можно переопределить метод __init__
            else:
                try:
                    my_obj = Worker.objects.get(account=request.user)
                except Worker.DoesNotExist:
                    my_obj = Worker(account=request.user)
                my_obj.first_name = str(my_dict['first_name'])
                my_obj.country = str(my_dict['country'])
                my_obj.city = str(my_dict['city'])
                my_obj.e_mail = str(my_dict['e_mail'])
                my_obj.second_name = str(my_dict['second_name'])
                my_obj.education = str(my_dict['education'])
                my_obj.work_experience = str(my_dict['work_experience'])
            if 7 <= len(my_dict['phone']) <= 16:
                my_obj.phone = int(my_dict['phone'])
            try:
                if my_dict['age'] and datetime(1900, 1, 1) <= datetime.strptime(str(my_dict['age']), "%d.%m.%Y") <= datetime.now():
                    my_obj.age = datetime.strptime(str(my_dict['age']), "%d.%m.%Y")
            except ValueError:
                pass  # сделать обработку
            my_obj.save()
            HttpRequest.method = 'get'
            return redirect('/home/')
        else:
            return redirect('/sign-in')
