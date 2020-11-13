from django.shortcuts import render, redirect
from django.views import View
from .models import Vacancy


class AllVacancy(View):

    def get(self, request, *args, **kwargs):
        search = None
        if request.GET.get('q'):
            search = str(request.GET.get('q'))
        else:
            search = ""
        return render(request, 'vacancy/all_vacancy.html', context={'vacancies': Vacancy.objects.filter(title__icontains=search)})

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
