from django.shortcuts import render, redirect
from django.views import View
from .models import Resume
import json
from django.core.serializers import serialize


class AllResume(View):

    def get(self, request, *args, **kwargs):
        search = None
        if request.GET.get('q'):
            search = str(request.GET.get('q'))
        else:
            search = ""
        resumes = Resume.objects.values()
        # for elem in list(serialize("json", Resume.objects.all())):
            # print('---'+elem+'------------------')
            # if search in elem['title']:
            #     resumes.append(elem)
        return render(request, 'resume/all_resume.html', context={'resumes': Resume.objects.all()})

    def post(self, request, *args, **kwargs):
        pass


class CreateResume(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'resume/create_resume.html')
        else:
            return redirect("sing-in/")

    def post(self, request, *args, **kwargs):
        pass
