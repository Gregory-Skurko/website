from django.contrib.auth import logout as standart_logout, authenticate, login as standart_login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from account_manager.forms import RegisterForm, AuthorizeForm, ChangePersonalInformationForm
from account_manager.models import User


def register(request):
    try:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')

        template = 'account_manager/register.html'
        args = {}

        if request.method == 'POST':
            pass
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
    template = 'account_manager/login.html'

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

    return render_to_response(template, args, context_instance=RequestContext(request))


def logout(request):
    standart_logout(request)
    return HttpResponseRedirect('/login')

def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    args = {}
    template = 'account_manager/profile.html'

    if request.method == 'POST':
        form = ChangePersonalInformationForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['email']:
                request.user.email = form.cleaned_data['email']
                request.user.save()

            if form.cleaned_data['new_password']:
                request.user.set_password(form.cleaned_data['new_password'])
                request.user.save()

            if form.cleaned_data['avatar']:
                request.user.avatar = form.cleaned_data['avatar']
                request.user.save()

    else:
        form = ChangePersonalInformationForm()

    args.update({'form': form})
    return render_to_response(template, args, context_instance=RequestContext(request))
