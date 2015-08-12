from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.core.validators import RegexValidator
from django.forms import ModelForm
from blog.models import User
from django.http import Http404


class CommentForm(forms.Form):
    body = forms.CharField(label='Text', widget=forms.Textarea(
        attrs={'class': 'materialize-textarea', 'id': 'body'}))


class RegisterForm(forms.Form):
    error_css_class = 'error'

    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    username = forms.CharField(required=True, validators=[alphanumeric],
                               widget=forms.TextInput(
                                    attrs={'id': 'username', 'class': 'validate'}))

    password = forms.CharField(required=True,
                                widget=forms.PasswordInput(
                                    attrs={'id': 'password', 'class': 'validate'}))

    password_confirm = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'id': 'password_confirm', 'class': 'validate'}))

    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'id': 'email', 'class': 'validate form-control', 'type': 'email'}))

    avatar = forms.ImageField(required=False,
                              widget=forms.FileInput(
                                  attrs={'id': 'avatar', 'class': 'validate', 'type': 'text'}))
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('%s already exists' % username)

    def clean(self):
        data = self.cleaned_data
        if "password" in data and "password_confirm" in data and data["password"] != data["password_confirm"]:
            raise forms.ValidationError("Passwords must be same")
        return data

class AuthorizeForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'username', 'class': 'validate'}),
        required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'validate'}),
        required=True)


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























