from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from blog.models import User


class CommentForm(forms.Form):
    body = forms.CharField(label='Comment', widget=forms.Textarea(
        attrs={'class': 'materialize-textarea', 'id': 'body'}))

class NewPostForm(forms.Form):
    title = forms.CharField(label='Title', required=True,
        widget=forms.TextInput(attrs={'id': 'title'}))
    body = forms.CharField(label='Body', required=True,
                           widget=forms.Textarea(attrs={'id': 'body', 'class': 'materialize-textarea'}))
    tags = forms.CharField(label='Tags', required=False,
        widget=forms.TextInput(attrs={'id': 'tags', 'class': 'validate', 'placeholder': 'List tags separated by space'}))

    VISIBLE_TYPE = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    visible = forms.ChoiceField(label='',
        widget=forms.RadioSelect(attrs={'id': 'radio'}),
        choices=VISIBLE_TYPE, initial='public')


class AdminUserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class AdminUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class SearchForm(forms.Form):
    REQUEST_TYPE = (
    ('tag', 'Tag'),
    ('user', 'User'),
    ('post', 'Post'),
    )

    request = forms.CharField(required=False, widget=forms.TextInput(attrs={'id': 'request', 'class': 'validate', 'placeholder': 'Request'}))
    request_type = forms.ChoiceField(choices=REQUEST_TYPE, widget=forms.Select(attrs={'class': 'browser-default'}))

























