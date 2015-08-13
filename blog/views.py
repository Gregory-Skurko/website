from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout as standart_logout, authenticate, login as standart_login
from django.core.exceptions import ValidationError
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from account_manager.models import User
from blog.forms import CommentForm, NewPostForm, SearchForm
from blog.models import Post, Comment, Tag


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


def add_post(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            new_post = Post(user=request.user, title=form.cleaned_data['title'], body=form.cleaned_data['body'])
            new_post.save()

            tags = form.cleaned_data['tags'].split()
            for tag in tags:
                new_tag = Tag(tag=tag)
                new_tag.save()
                new_post.tag.add(tag)
            return HttpResponseRedirect('/' + request.user.username + '/post' + str(new_post.id))
    else:
        form = NewPostForm()

    return render_to_response('blog/add-post.html', {'form': form}, context_instance=RequestContext(request))


def search(request, search_request=None, type_request=None):
    template = 'blog/search.html'
    args = {}

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            request_type = form.cleaned_data['request_type']
            if request_type == 'tag':
                existing_tags = [t.tag for t in Tag.objects.all()]
                tags = [tag for tag in form.cleaned_data['request'].split() if tag in existing_tags]
                list_post = []

                for post in Post.objects.all():
                    post_tags = [t.tag for t in post.tag.all()]

                    if all(tag in post_tags for tag in tags):
                        list_post.append(post)

                args.update({'posts': list_post})
            elif request_type == 'user':
                args.update({'posts': Post.objects.filter(user=User.objects.get(username=form.cleaned_data['request']))})
            elif request_type == 'post':
                args.update({'posts': Post.objects.filter(title=form.cleaned_data['request'])})
    else:
        list_post = []
        for post in Post.objects.all():
            post_tags = [t.tag for t in post.tag.all()]
            if search_request in post_tags:
                list_post.append(post)
        args.update({'posts': list_post})
        form = SearchForm()

    args.update({'user': request.user})
    args.update({'form': form})
    return render_to_response(template, args)
























