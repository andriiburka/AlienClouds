from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from alienclouds_app.forms.projects import UploadItemForm, UploadProjectForm
from alienclouds_app.forms.users import CreateUserForm
from alienclouds_app.models import *

'''
#  ███╗   ██╗  █████╗  ██╗   ██╗     ██████╗   █████╗  ██████╗
#  ████╗  ██║ ██╔══██╗ ██║   ██║     ██╔══██╗ ██╔══██╗ ██╔══██╗
#  ██╔██╗ ██║ ███████║ ██║   ██║     ██████╔╝ ███████║ ██████╔╝
#  ██║╚██╗██║ ██╔══██║ ╚██╗ ██╔╝     ██╔══██╗ ██╔══██║ ██╔══██╗
#  ██║ ╚████║ ██║  ██║  ╚████╔╝      ██████╔╝ ██║  ██║ ██║  ██║
#  ╚═╝  ╚═══╝ ╚═╝  ╚═╝   ╚═══╝       ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═╝
#  Comment:
'''


def index(request):
    context = {
        'index_title': 'ALIENCLOUDS',
        'users': User.objects.all(),
        'count_users': User.objects.all().count(), }
    return render(request, 'index.html', context)


class IndexListView(ListView):
    if User.is_superuser:
        model = User
        template_name = 'index_class_views.html'
        queryset = User.objects.all().order_by('first_name')

        def get_context_object_name(self, object_list):
            return 'class_users'

        def get_context_data(self, *, object_list=None, **kwargs):
            context_dict = super().get_context_data()
            context_dict['title'] = 'Class Title'
            return context_dict


'''
#   █████╗  ██╗   ██╗ ████████╗ ██╗  ██╗
#  ██╔══██╗ ██║   ██║ ╚══██╔══╝ ██║  ██║
#  ███████║ ██║   ██║    ██║    ███████║
#  ██╔══██║ ██║   ██║    ██║    ██╔══██║
#  ██║  ██║ ╚██████╔╝    ██║    ██║  ██║
#  ╚═╝  ╚═╝  ╚═════╝     ╚═╝    ╚═╝  ╚═╝________________________________________________________________________________
#  Comment:
'''


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                firstname = form.cleaned_data.get('first_name')
                firstname_or_username = firstname if firstname else username
                messages.success(request, f'Account for {firstname_or_username} is created')
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
            # gets username and password from login forms and assigns them to the variable user
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                login(request, user)
                return redirect('projects')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {
            'login_title': 'Login | ALIENCLOUDS',
        }
        return render(request, 'auth/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


'''
#  ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗███████╗
#  ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝██╔════╝
#  ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   ███████╗
#  ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   ╚════██║
#  ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   ███████║
#  ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   ╚══════╝___________________________________________________
#   Comment:
'''


@login_required(login_url='login')
def upload_project(request):
    if request.method == 'GET':
        context = {
            'form': UploadProjectForm()
        }
        return render(request, 'crud/projects/upload_project.html', context)
    else:
        form = UploadProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('projects')
        context = {
            'form': form,
        }
        return render(request, 'crud/projects/upload_project.html', context)


def projects(request):
    if request.method == 'GET':
        context = {
            'projects_title': 'Projects | ALIENCLOUDS',
            'projects': Project.objects.all(),
        }
        return render(request, 'pages/projects.html', context)


def project_details(request, pk):
    context = {'project': Project.objects.get(pk=pk), }
    return render(request, 'crud/projects/project_details.html', context)


def project_edit(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'GET':
        context = {'form': UploadProjectForm(instance=project),
                   'project': project, }
        return render(request, 'crud/projects/project_edit.html', context)
    else:
        form = UploadProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        context = {'form': form,
                   'recipe': project, }
        return render(request, 'crud/projects/project_edit.html', context)


def project_delete(request, pk):
    obj = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('projects')
    return render(request, "crud/projects/project_delete.html")


'''
#  ███████╗██╗  ██╗ ██████╗ ██████╗
#  ██╔════╝██║  ██║██╔═══██╗██╔══██╗
#  ███████╗███████║██║   ██║██████╔╝
#  ╚════██║██╔══██║██║   ██║██╔═══╝
#  ███████║██║  ██║╚██████╔╝██║
#  ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝----------------------------------------------------------------------------------------
#   Comment: 
'''


def store(request):
    context = {'title': 'SHOP | ALIENCLOUDS',
               'items': ShopItem.objects.all(),
               'image': ShopItem.image, }
    return render(request, 'pages/store.html', context)


@login_required(login_url='login')
def upload_item(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            context = {
                'upload_form': UploadItemForm()
            }
            return render(request, 'crud/shop/upload_item.html', context)


def item_details(request, pk):
    context = {'item': ShopItem.objects.get(pk=pk), }
    return render(request, 'crud/shop/item_details.html', context)


def item_edit(request, pk):
    item = ShopItem.objects.get(pk=pk)
    if request.method == 'GET':
        context = {'form': UploadItemForm(instance=item),
                   'item': item, }
        return render(request, 'crud/shop/item_edit.html', context)
    else:
        form = UploadItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('shop')
        context = {'form': form,
                   'recipe': item, }
        return render(request, 'crud/shop/item_edit.html', context)


def item_delete(request, pk):
    obj = get_object_or_404(ShopItem, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('shop')
    return render(request, "crud/shop/item_delete.html")
