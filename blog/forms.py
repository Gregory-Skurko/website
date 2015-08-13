from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from django.forms import ModelForm
from blog.models import User
from django.http import Http404


class CommentForm(forms.Form):
    body = forms.CharField(label='Text', widget=forms.Textarea(
        attrs={'class': 'materialize-textarea', 'id': 'body'}))

class NewPostForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'title', 'class': 'validate'}), required=True)
    body = forms.CharField(widget=forms.Textarea(attrs={'id': 'body', 'class': 'materialize-textarea'}),
                           required=True)
    tags = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'tags', 'class': 'validate'}), required=True)


class AdminUserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class AdminUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
































