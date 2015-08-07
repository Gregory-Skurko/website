from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import Http404


class CommentForm(forms.Form):
    body = forms.CharField(label='Text', widget=forms.Textarea(
        attrs={'class': 'form-control',
               'id': 'body',
               'placeholder': 'Text', }))


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'username', 'placeholder': 'Username', 'class': 'form-control'}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password1', 'placeholder': 'Password', 'class': 'form-control'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password2', 'placeholder': 'Password Confirmation', 'class': 'form-control'}), required=True)

    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'id': 'email', 'class': 'form-control', 'placeholder': 'Email'}))
    img = forms.ImageField(required=False, widget=forms.FileInput(attrs={'id': 'img', 'class': 'form-control', 'placeholder': 'Img'}))

class AuthorizeForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'username', 'placeholder': 'Username', 'class': 'form-control'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password', 'placeholder': 'Password', 'class': 'form-control'}), required=True)


class NewPostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'id': 'title', 'placeholder': 'Title', 'class': 'form-control'}), required=True)
    body = forms.CharField(widget = forms.Textarea(attrs={'id': 'body', 'placeholder': 'Body', 'class': 'form-control'}), required=True)























