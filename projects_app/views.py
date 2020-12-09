from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from .models.project import *

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
    }
    return render(request, 'pages/projects.html', context)


@login_required(login_url='login')
def upload(request):
    return render(request, 'pages/upload.html')