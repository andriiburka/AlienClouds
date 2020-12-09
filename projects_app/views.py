from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from .forms import ProjectUploadForm
from projects_app.models import *


#
#
#  ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗███████╗
#  ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝██╔════╝
#  ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   ███████╗
#  ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   ╚════██║
#  ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   ███████║
#  ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   ╚══════╝


def all_projects(request):
    context = {
        'projects_title': 'Projects | ALIENCLOUDS',
        'projects': Project.objects.all(),
        'images': Project.image,
    }
    return render(request, 'pages/projects.html', context)


@login_required(login_url='login')
def my_profile(request):
    return render(request, 'users/my-profile.html')


def project(request):
    if request.method == 'POST':
        context = {
            'projects': Project.objects.all,
            'form': ProjectUploadForm(),

        }
        return render(request, 'users/my-profile.html', context)
