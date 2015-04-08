# coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from Work_Manager.tasks_manager.models import UserProfile


def user_login(request):
    if request.method == 'POST':
        try:
            m = UserProfile.objects.get(login=request.POST['login_name'])
            if m.password == request.POST['password']:
                request.session['user_id'] = m.id
                return HttpResponseRedirect(reversed('public_index'))
        except UserProfile.DoesNotExist:
            return HttpResponse("your username and password didn't match.")


def user_logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse("you're logged out.")


def register():
    pass






