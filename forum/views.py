from django.shortcuts import render, get_object_or_404
from .models import ForumThread, ForumPost
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.utils.text import slugify
# Create your views here.


def login(request):
    return render(request, 'forum/login.html', {'user': request.user, 'request': request})


def get_forum_thread():
    return ForumThread.objects.order_by('-pub_date')


def index(request):
    gft = get_forum_thread()
    return render(request, 'forum/index.html', {'user': request.user, 'threads':gft})


@login_required
def newthread(request):
    try:
        title = request.POST['title']
        body = request.POST['body']
    except KeyError:
        raise Http404
    now = timezone.now()
    slug = slugify(title)

    thread = ForumThread(title=title, slug=slug, pub_date=now)
    thread.save()

    post = ForumPost(thread=thread, text=body, pub_date=now, author=request.user)
    post.save()

    return HttpResponseRedirect(reverse('forums:index'))