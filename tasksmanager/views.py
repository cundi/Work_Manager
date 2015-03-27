# -*- coding:utf-8 -*-

import re

from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Project, Task, Supervisor, Developer, UserProfile
import json
# Create your views here.


def task_list(request):
        task = Task.objects.filter()
        context_dict = {'task': task}
        return render(request, 'task_list.html', context_dict)


def task_detail(request, pk):
    single_task = Task.objects.get(pk=pk)
    return render(request, 'task_detail.html', {'task': single_task})


@csrf_exempt
def task_ajax(request):
    if request.method == 'GET' and request.is_ajax():
        try:
            form_task = request.GET.get('query', '')
        except ValueError:
            return HttpResponse('form task is not exist')
        try:
            task = Task.objects.filter(title__icontains=form_task)
        except ValueError:
            return HttpResponse('task content is not write down yet')
        pre_json_list = []
        for i in task:
            pre_json_list.append({
                'title': i.title,
                'description': i.description,
                'developer': i.developer.supervisor.name
            })
        recipe_list_json = json.dumps(pre_json_list)
        return HttpResponse(recipe_list_json, content_type='application/javascript')
    else:
        return HttpResponse('client ajax request is not working')

def index(request):
    queryset = Project.objects.all()
    task = Task.objects.filter()
    context_dict = \
        {
            'queryset': queryset, 'action': "Display all project", 'search': u'全局搜索',
            'task': task,
        }
    return render(request, 'index.html', context_dict)


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'project_detail.html', {'project': project})


# class Update_Project(FormView):
# template_name = 'project_list.html'
# form_class = ProjectForm
# success_url = '/'
#
#     def form_valid(self, form):
#         form.send_email()
#         return super(Update_Project, self).form_valid(form)


class UpdateProjectList(ListView):
    model = Project
    context_object_name = 'projects'


def create_project(request):
    input_name = ['title', 'description', 'client_name']
    projects = Project.objects.all()
    context_dict = {'projects': projects}
    if request.POST:
        for x in input_name:
            if x in request.POST:
                title = request.POST.get('title', '')
                if title == '':
                    return HttpResponse(u'项目名称不能为空')
                description = request.POST.get('description', '')
                client_name = request.POST.get('client_name', '')
                new_project = Project(
                    title=title, description=description, client_name=client_name)
                new_project.save()
                return HttpResponse(u'添加项目已经保存')
    else:
        return render(request, 'create_project.html', context_dict)


def project_list(request):
    return render(request, 'project_list.html')


def create_developer(request, ):
    input_name = ['name', 'login', 'password', 'supervisor']
    u = UserProfile.objects.filter()
    if request.POST:
        for x in input_name:
            if x in request.POST:
                name = request.POST.get('name', '')
                if name == '':
                    er = {"errors": "your name can't leave a blank here!"}
                    return (er)
                for user in u.values():
                    if name in user['name']:
                        return HttpResponse("the name is already exist")
                login = request.POST.get('login', '')
                if login == '':
                    return HttpResponse("your login name is blank, conform it! ")
                password = request.POST.get('password', '')
                if password == '':
                    return HttpResponse("your password is a blank, correct it!")
                supervisor_id = request.POST.get('supervisor', '')
                supervisor = Supervisor.objects.get(id=supervisor_id)
                new_dev = Developer(
                    name=name, login=login, password=password, supervisor=supervisor)
                new_dev.save()
                return HttpResponse("Developer added")
    else:
        supervisors_list = Supervisor.objects.all()
        context_dict = {'supervisors_list': supervisors_list}
        return render(request, 'create_developer.html', context_dict)


def connection(request):
    return render(request, 'connection.html')


def create_task(request):
    t = Task.objects.all()
    context_dict = {'tasks': t}
    return render(request, 'create_task.html', context_dict)


def create_supervisor(request):
    # supervisors = Supervisor.objects.all()
    # context_dict = {'supervisors': supervisors}
    input_name = ['spv_name', 'spv_login', 'spv_password', 'spv_password_2', 'spv_born_date', 'spv_phone',
                  'spv_email', 'spv_years_seniority', 'spv_specialisation']
    errors = []

    if request.POST:
        for i in input_name:
            if i in request.POST:
                name = request.POST.get('spv_name', '')
                u_name = UserProfile.objects.filter(name=name)
                if not re.search(r'^\w+$', name):
                    errors.append(u'密码不匹配规则')
                login = request.POST.get('spv_login', '')
                password = request.POST.get('spv_password', '')
                password_bis = request.POST.get('spv_password_2', '')
                phone = request.POST.get('spv_phone', '')
                email = request.POST.get('spv_email', '')
                born_date = request.POST.get('spv_born_date', '')
                years_seniority = request.POST.get('spv_years_seniority', '')
                specialisation = request.POST.get('spv_specialisation', '')
                if not password == password_bis:
                    return HttpResponse(u'两次密码不相等')
                if email == u_name[0].__dict__['email']:
                    errors.append(u'该邮箱已经被注册')
                new_supervisor = Supervisor(name=name, login=login, password=password, password_bis=password_bis,
                                            phone=phone,
                                            email=email, born_date=born_date, years_seniority=years_seniority,
                                            specialisation=specialisation
                                            )
                new_supervisor.save()
                return render(request, 'create_supervisor.html', {'errors': errors})
    else:
        return render(request, 'create_supervisor.html', )
