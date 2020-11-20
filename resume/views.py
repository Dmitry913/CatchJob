from django.shortcuts import render, redirect
from django.views import View
from .models import Resume
import json
from django.core.serializers import serialize
from django.http import HttpResponse
from main_app.models import Worker


class AllResume(View):

    def get(self, request, *args, **kwargs):
        search = None
        if request.GET.get('q'):
            search = str(request.GET.get('q'))
        else:
            search = ""
        # resumes = Resume.objects.values()
        return render(request, 'resume/all_resume.html', context={'resumes': Resume.objects.filter(title__icontains=search)})

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


class InfProfile(View):

    def get(self, request, my_title, *args, **kwargs):
        my_user = Resume.objects.get(title=my_title).author
        profile = Worker.objects.filter(account=my_user)
        return render(request, 'resume/profile_work.html', context={"data": profile,
                                                                    "resume": Resume.objects.filter(title=my_title)})
