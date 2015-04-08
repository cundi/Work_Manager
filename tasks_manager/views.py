# -*- coding:utf-8 -*-

import re
import json
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
# from django.views.decorators.csrf import csrf_exempt
from .models import Project, Task, Supervisor, Developer, UserProfile
# from django.contrib.auth.decorators import login_required, permission_required
# from django.contrib.auth import authenticate, login, logout
# from django.utils.decorators import method_decorator
from django.views.generic import ListView, View
# from Work_Manager.utils import anti_resubmit
# Create your views here.

try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps  # Python 2.4 fallback.
import random
from django.conf import settings
from django.utils.decorators import available_attrs
from hashlib import md5 as md5_constructor

if hasattr(random, 'SystemRandom'):
    randrange = random.SystemRandom().randrange
else:
    randrange = random.randrange
_MAX_CSRF_KEY = 18446744073709551616L     # 2 << 63


def _get_new_submit_key():
    return md5_constructor("%s%s" % (randrange(0, _MAX_CSRF_KEY), settings.SECRET_KEY)).hexdigest()


def anti_resubmit(page_key=''):
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if request.method == 'GET':
                request.session['%s_submit' % page_key] = _get_new_submit_key()
                print 'session:' + request.session.get('%s_submit' % page_key)
            elif request.method == 'POST':
                old_key = request.session.get('%s_submit' % page_key, '')
                if old_key == '':
                    return HttpResponseRedirect(reverse_lazy('public_index'))
                request.session['%s_submit' % page_key] = ''
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


def login_required():
    pass


# @anti_resubmit(page_key='user_login')
def user_login(request):
    login_status = []
    if request.method == 'POST':
        try:
            m = UserProfile.objects.get(login=request.POST['login_name'])
            if m.password == request.POST['login_password']:
                request.session['user_id'] = m.id
                login_status.append('allow_login')
                return HttpResponseRedirect(reverse_lazy('accounts:user_profile'))
        except UserProfile.DoesNotExist:
            return HttpResponse("your username and password didn't match.")
    else:
        return render(request, 'accounts/login.html', )


def user_logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse_lazy('public_index'))


def user_profile(request):
    return render(request, 'user_profile.html')


def task_list(request):
    tasks = Task.objects.filter()
    return render(request, 'task_list.html', {'tasks':tasks})


def task_detail(request, pk):
    single_task = Task.objects.get(pk=pk)
    return render(request, 'task_detail.html', {'task': single_task})


def task_ajax(request):
    if request.method == 'GET' and request.is_ajax():
        try:
            form_task = request.GET.get('query', '')
        except ValueError:
            return HttpResponse('form task is not exist')
        task = Task.objects.filter(title__icontains=form_task)
        if not task:
            return JsonResponse({'errors': '没有查到任何内容，请检查您输入的内容是否为task的名称'}, safe=False)
        pre_json_list = []
        for i in task:
            pre_json_list.append({
                'id': i.id,
                'title': i.title,
                'description': i.description,
                'developer': i.developer.supervisor.name
            })
        return JsonResponse(pre_json_list, safe=False)
    if request.method == 'POST' and request.is_ajax():
        return HttpResponse('client ajax request is not working')


def task_delete(request):
    pass


def index(request):
    queryset = Project.objects.all()
    task = Task.objects.filter()
    context_dict = \
        {
            'queryset': queryset, 'action': "目前开发的项目", 'search': u'全局搜索',
            'task': task,
        }
    return render(request, 'index.html', context_dict)


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'project_detail.html', {'project': project})


class UpdateProjectList(ListView):
    model = Project
    context_object_name = 'projects'


def create_project(request):
    input_name = ['title', 'description', 'client_name']
    projects = Project.objects.all()
    context_dict = {'projects': projects}
    errors = []
    if request.POST:
        for x in input_name:
            if x in request.POST:
                title = request.POST.get('title', '')
                if title == '':
                    errors.append('title is not allow leaving a blank')
                description = request.POST.get('description', '')
                client_name = request.POST.get('client_name', '')
                new_project = Project(
                    title=title, description=description, client_name=client_name)
                new_project.save()
                return render(request, 'create_project', {'errors': errors})
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
                    return er
                for user in u.values():
                    if name in user['name']:
                        return HttpResponse("the name is already exist")
                login = request.POST.get('login', '')
                if not login:
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
