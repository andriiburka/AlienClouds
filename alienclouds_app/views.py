from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from alienclouds_app.forms.projects import UploadItemForm, UploadProjectForm
from alienclouds_app.forms.users import CreateUserForm
from alienclouds_app.models import *


#
#
#
#
#
#  ███╗   ██╗  █████╗  ██╗   ██╗     ██████╗   █████╗  ██████╗
#  ████╗  ██║ ██╔══██╗ ██║   ██║     ██╔══██╗ ██╔══██╗ ██╔══██╗
#  ██╔██╗ ██║ ███████║ ██║   ██║     ██████╔╝ ███████║ ██████╔╝
#  ██║╚██╗██║ ██╔══██║ ╚██╗ ██╔╝     ██╔══██╗ ██╔══██║ ██╔══██╗
#  ██║ ╚████║ ██║  ██║  ╚████╔╝      ██████╔╝ ██║  ██║ ██║  ██║
#  ╚═╝  ╚═══╝ ╚═╝  ╚═╝   ╚═══╝       ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═╝
#  Comment:


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


#
#
#
#
#
#   █████╗  ██╗   ██╗ ████████╗ ██╗  ██╗
#  ██╔══██╗ ██║   ██║ ╚══██╔══╝ ██║  ██║
#  ███████║ ██║   ██║    ██║    ███████║
#  ██╔══██║ ██║   ██║    ██║    ██╔══██║
#  ██║  ██║ ╚██████╔╝    ██║    ██║  ██║________________________________________________________________________________
#  ╚═╝  ╚═╝  ╚═════╝     ╚═╝    ╚═╝  ╚═╝
#  Comment:


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
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            # gets username and password from login forms and assigns it to the variable user
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                # executes django method 'login'
                login(request, user)
                return redirect('upload_project')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {
            'login_title': 'Login | ALIENCLOUDS',
        }
        return render(request, 'auth/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


#
#
#
#
#
#  ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗███████╗
#  ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝██╔════╝
#  ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   ███████╗
#  ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   ╚════██║
#  ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   ███████║___________________________________________________
#  ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   ╚══════╝


@login_required(login_url='login')
def upload_project(request):
    if request.method == 'GET':
        context = {
            'form': UploadProjectForm()
        }
        return render(request, 'pages/upload_project.html', context)
    else:
        form = UploadProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('projects')
        context = {
            'form': form,
        }
        return render(request, 'pages/upload_project.html', context)


def projects(request):
    if request.method == 'GET':
        context = {
            'projects_title': 'Projects | ALIENCLOUDS',
            'projects': Project.objects.all(),
        }
        return render(request, 'pages/projects.html', context)


def project_details(request, pk):
    context = {'project': Project.objects.get(pk=pk), }
    return render(request, 'pages/project_details.html', context)


def project_edit(request, pk):
    context = {}
    obj = get_object_or_404(Project, pk=pk)
    form = UploadProjectForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(f'/project_details/{pk}/')

    context["form"] = form
    return render(request, "pages/project_edit.html", context)
#
#
#
#
#
#  ███████╗██╗  ██╗ ██████╗ ██████╗
#  ██╔════╝██║  ██║██╔═══██╗██╔══██╗
#  ███████╗███████║██║   ██║██████╔╝
#  ╚════██║██╔══██║██║   ██║██╔═══╝
#  ███████║██║  ██║╚██████╔╝██║_________________________________________________________________________________________
#  ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝
#


@login_required(login_url='login')
def upload_item(request):
    if request.method == 'GET':
        context = {
            'upload_form': UploadItemForm()
        }
        return render(request, 'pages/upload_item.html', context)


def shop(request):
    context = {
        'title': 'SHOP | ALIENCLOUDS',
        'items': ShopItem.objects.all(),
        'image': ShopItem.image,
    }
    return render(request, 'pages/shop.html', context)


def item_details(request, pk):
    context = {
        'item': ShopItem.objects.get(pk=pk)
    }
    return render(request, 'pages/item_details.html', context)
