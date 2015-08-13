from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout as standart_logout, authenticate, login as standart_login
from django.core.exceptions import ValidationError
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from blog.forms import CommentForm, RegisterForm, AuthorizeForm, NewPostForm, ChangePersonalInformationForm
from blog.models import Post, Comment, Tag, User


def posts(request, username=None):
    try:
        args = {}
        if username is None:
            posts = Post.objects.all()
        else:
            posts = Post.objects.reverse().filter(user=User.objects.get(username=username))

        if len(posts) == 0:
            args.update({'empty': True})
        else:
            args.update({'posts': posts})

        args.update({'user': request.user})
    except:
        raise Http404()

    return render_to_response("blog/posts.html", args)


def post(request, username, post_id):
    try:
        args = {}
        args.update({'post': Post.objects.get(id=post_id)})
        args.update({'comments': Comment.objects.filter(post=post_id)})
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                Comment(post=Post.objects.get(id=post_id), user=User.objects.get(username=request.user.username),
                        body=form.cleaned_data['body']).save()
                return HttpResponseRedirect('/' + username + '/post' + post_id)
        else:
            form = CommentForm()
        args.update({'form': form})
    except:
        raise Http404()

    return render_to_response("blog/post.html", args, context_instance=RequestContext(request))


def register(request):
    try:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')

        template = 'blog/register.html'
        args = {}
        if request.method == 'POST':
            form = RegisterForm(request.POST, request.FILES)
            if form.is_valid():
                user = User(username=form.cleaned_data['username'],
                            password=make_password(form.cleaned_data['password']),
                            email=form.cleaned_data['email'],
                            avatar=form.cleaned_data['avatar'])

                user.save()
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                standart_login(request, user)
                return HttpResponseRedirect('/' + request.POST['username'])
            else:
                args.update({'error': True})
        else:
            form = RegisterForm()

        args.update({'form': form})
    except:
        raise Http404()
    return render_to_response(template, args, context_instance=RequestContext(request))


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/' + request.user.username)

    args = {}
    if request.method == 'POST':
        form = AuthorizeForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                standart_login(request, user)
                return HttpResponseRedirect('/' + request.POST['username'])

        args.update({'error': True})
    else:
        form = AuthorizeForm()

    args.update({'form': form})

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
            tags = form.cleaned_data['tags'].split()
            new_post.save()

            for tag in tags:
                new_tag = Tag(tag=tag)
                new_tag.save()
                new_post.tag.add(tag)
            return HttpResponseRedirect('/' + request.user.username + '/post' + str(new_post.id))
    else:
        form = NewPostForm()

    return render_to_response('blog/add-post.html', {'form': form}, context_instance=RequestContext(request))


def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    args = {}
    if request.method == 'POST':
        form = ChangePersonalInformationForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            request.user.set_password(form.cleaned_data['new_password'])
            request.user.save()
    else:
        form = ChangePersonalInformationForm()

    args.update({'form': form})
    return render_to_response('blog/profile.html', args, context_instance=RequestContext(request))


def search(request, search_request=None, type_request=None):
    return render_to_response('blog/search.html')



























