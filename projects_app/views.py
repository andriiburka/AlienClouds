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
    return render(request, 'projects_app/allprojects.html', context)


@login_required(login_url='login')
def upload_project(request):
    if request.method == 'GET':
        context = {
            'projects': Project.objects.all,
            'project_form': ProjectUploadForm(),
        }
        return render(request, 'projects_app/upload_project.html', context)


def project_details(request):
    context = {
    }
    return render(request, 'projects_app/project_details.html', context)
