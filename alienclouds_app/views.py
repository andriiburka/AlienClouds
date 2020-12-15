from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView

# Inherits the class UserCreationForm but now it has an email form
from .forms import CreateUserForm  # CMD+Click to visit this class

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from alienclouds_app.forms import ProjectUploadForm
from alienclouds_app.models import *


#  ███╗   ██╗  █████╗  ██╗   ██╗     ██████╗   █████╗  ██████╗
#  ████╗  ██║ ██╔══██╗ ██║   ██║     ██╔══██╗ ██╔══██╗ ██╔══██╗
#  ██╔██╗ ██║ ███████║ ██║   ██║     ██████╔╝ ███████║ ██████╔╝
#  ██║╚██╗██║ ██╔══██║ ╚██╗ ██╔╝     ██╔══██╗ ██╔══██║ ██╔══██╗
#  ██║ ╚████║ ██║  ██║  ╚████╔╝      ██████╔╝ ██║  ██║ ██║  ██║
#  ╚═╝  ╚═══╝ ╚═╝  ╚═╝   ╚═══╝       ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═╝


def index(request):
    context = {
        'index_title': 'ALIENCLOUDS',
        'users': User.objects.all(),
        'count_users': User.objects.all().count(),
    }
    return render(request, 'pages/index.html', context)


class IndexListView(ListView):
    model = User
    template_name = 'index_class_views.html'
    queryset = User.objects.all().order_by('first_name')

    def get_context_object_name(self, object_list):
        return 'class_users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data()
        context_dict['title'] = 'Class Title'
        return context_dict


def contacts(request):
    alienclouds = '<iframe style="padding-top: 50px; text-align: center; width: 350px; height: 500px" src="https://discord.com/widget?id=780048729037340673&theme=dark" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe>'
    softuni_pythhon_path = '<iframe style="padding-top: 50px; text-align: center; width: 350px; height: 500px" src="https://discord.com/widget?id=699289734282739732&theme=dark" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe>'
    context = {
        'title': 'Contacts | ALIENCLOUDS',
        'discord_servers': [alienclouds, softuni_pythhon_path]
    }
    return render(request, 'pages/contacts.html', context)


#   █████╗  ██╗   ██╗ ████████╗ ██╗  ██╗
#  ██╔══██╗ ██║   ██║ ╚══██╔══╝ ██║  ██║
#  ███████║ ██║   ██║    ██║    ███████║
#  ██╔══██║ ██║   ██║    ██║    ██╔══██║
#  ██║  ██║ ╚██████╔╝    ██║    ██║  ██║
#  ╚═╝  ╚═╝  ╚═════╝     ╚═╝    ╚═╝  ╚═╝
#
def registerPage(request):
    """ register page - everyone can visit"""
    if request.user.is_authenticated:  # for example if you are logged in no sense to login again SO redirect to index
        return redirect('index')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Account for {user} is created.')
                return redirect('login')
            else:
                messages.error(request, 'Error occurred, try again')
                return redirect('register')
        else:
            form = CreateUserForm()
        context = {'form': form}
        return render(request, 'auth/register.html', context)


def loginPage(request):
    """ register page - everyone can visit"""
    # if user is logged in
    if request.user.is_authenticated:
        # no sense to login again so redirect to homepage
        return redirect('index')
    else:
        if request.method == 'POST':
            # gets username and password from login forms and assigns it to the variable user
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                # executes django method 'login'
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {
            'login_title': 'Login | ALIENCLOUDS',
        }
        return render(request, 'auth/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index')


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
    return render(request, '../templates/pages/allprojects.html', context)


def project_details(request, pk):
    context = {
        'project': Project.objects.get(pk=pk)
    }
    return render(request, '../templates/pages/project_details.html', context)


@login_required(login_url='login')
def upload_project(request):
    if request.method == 'GET':
        context = {
            'projects': Project.objects.all,
            'project_form': ProjectUploadForm(),
        }
        return render(request, '../templates/pages/upload_project.html', context)
