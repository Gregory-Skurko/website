from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import logout as standart_logout, authenticate, login as standart_login
from django.core.urlresolvers import reverse
from django.db.models import QuerySet
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.template.context_processors import csrf
from django.views.decorators.http import require_http_methods
from blog.forms import CommentForm, RegisterForm, AuthorizeForm, NewPostForm
from blog.models import Post, Comment, Avatar


def index(request):
    try:
        objects = Post.objects.all()
        if len(objects) > 5:
            posts = objects[len(objects) - 5:]
        else:
            posts = objects
    except:
        raise Http404()

    return render_to_response("blog/user_posts.html", {'posts': posts})

def user_posts(request, username):
    try:
        current_user = User.objects.get(username=username)
        posts = Post.objects.reverse().filter(user=current_user)
    except:
        raise Http404()

    return render_to_response("blog/user_posts.html", {'posts': posts})


def post(request, username, post_id):
    try:
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post=post_id)
    except:
        raise Http404()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            Comment(post=Post.objects.get(id=post_id), author=comment_form.cleaned_data['author'],
                    body=comment_form.cleaned_data['body']).save()
            return HttpResponseRedirect('/' + username + '/post' + post_id)
    else:
        comment_form = CommentForm()

    return render_to_response("blog/post.html", {'post': post, 'comments': comments, 'form': comment_form},
                              context_instance=RequestContext(request))

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/'+request.user.username)

    template = 'blog/register.html'
    args = {}
    if request.method == 'POST':
        new_user_form = RegisterForm(request.POST)

        if new_user_form.is_valid() and new_user_form.cleaned_data['password1'] == new_user_form.cleaned_data['password2']:
            user = User(username=new_user_form.cleaned_data['username'],
                        password=make_password(new_user_form.cleaned_data['password1']),
                        email=new_user_form.cleaned_data['email'])
            user.save()
            img = Avatar(user=user, img=new_user_form.cleaned_data['img'])
            img.save()
            return HttpResponseRedirect('/register')
        else:
            args.update({'post': True})

    else:
        new_user_form = RegisterForm()

    args.update({'form': new_user_form})

    return render_to_response(template, args, context_instance=RequestContext(request))

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/'+request.user.username)

    args = {}
    if not request.user.is_authenticated() and request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            standart_login(request, user)
            return HttpResponseRedirect('/'+request.POST['username'])
        else:
            return HttpResponseRedirect('/login')
    else:
        login_form = AuthorizeForm()

    args.update({'form': login_form})

    return render_to_response('blog/login.html', args, context_instance=RequestContext(request))

def logout(request):
    standart_logout(request)
    return HttpResponseRedirect('/login')

def add_post(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            new_post = Post(user=request.user, title=form.cleaned_data['title'], body=form.cleaned_data['body'])
            new_post.save()
            return HttpResponseRedirect('/'+request.user.username+'/post'+str(new_post.id))
    else:
        form = NewPostForm()

    return render_to_response('blog/add-post.html', {'form': form}, context_instance=RequestContext(request))


























