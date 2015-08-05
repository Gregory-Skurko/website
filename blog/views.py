from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response

# Create your views here.
from blog.models import Post, Comment


def index(request):
    try:
        posts = Post.objects.all()
    except:
        raise Http404()

    return render_to_response("blog/index.html", {'posts': posts, })


def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post=post_id)
    except:
        raise Http404()

    return render_to_response("blog/post.html", {'post': post, 'comments': comments})






















