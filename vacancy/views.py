from django.shortcuts import render, redirect
from django.views import View
from .models import Vacancy


class AllVacancy(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/all_vacancy.html', context={'vacancies': Vacancy.objects.all()})

    def post(self, request, *args, **kwargs):
        pass


class CreateVacancy(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'vacancy/create_vacancy.html')
        else:
            return redirect("sing-in/")

    def post(self, request, *args, **kwargs):
        pass
