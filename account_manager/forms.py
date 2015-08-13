from django import forms
from django.core.validators import RegexValidator
from account_manager.models import User

class RegisterForm(forms.Form):
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
        attrs={'id': 'email', 'class': 'validate', 'type': 'email'}))

    avatar = forms.ImageField(required=False,
                              widget=forms.FileInput(
                                  attrs={'id': 'avatar', 'class': 'validate'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('%s already exists' % username)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('%s already exists' % email)

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar', False)
        if avatar:
            max_size = 4 * 1024 * 1024
            if avatar._size > max_size:
                raise forms.ValidationError("Image file too large ( > 4mb )")
            else:
                return avatar

    def clean(self):
        data = self.cleaned_data
        if "password" in data and "password_confirm" in data and data["password"] != data["password_confirm"]:
            raise forms.ValidationError("Passwords must be same")
        return data


class ChangePersonalInformationForm(forms.Form):
    old_password = forms.CharField(required=False,
                                   widget=forms.PasswordInput(
                                       attrs={'id': 'old_password', 'class': 'validate'}))

    new_password = forms.CharField(required=False,
                                   widget=forms.PasswordInput(
                                       attrs={'id': 'new_password', 'class': 'validate'}))

    password_confirm = forms.CharField(required=False, widget=forms.PasswordInput(
        attrs={'id': 'password_confirm', 'class': 'validate'}))

    email = forms.EmailField(required=False, widget=forms.TextInput(
        attrs={'id': 'email', 'class': 'validate', 'type': 'email'}))

    avatar = forms.ImageField(required=False,
                              widget=forms.FileInput(
                                  attrs={'id': 'avatar', 'class': 'validate'}))

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(ChangePersonalInformationForm, self).__init__(*args, **kwargs)

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar', False)
        if avatar:
            max_size = 4 * 1024 * 1024
            if avatar._size > max_size:
                raise forms.ValidationError("Image file too large ( > 4mb )")
            else:
                return avatar

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('%s already exists' % email)

    def clean(self):
        data = self.cleaned_data
        if data['old_password'] == data['new_password'] == data['password_confirm'] == '':
            return data
        else:
            if data['old_password'] == '' \
                    or data['new_password'] == '' \
                    or data['password_confirm'] == '':
                raise forms.ValidationError("Fill the all fields")

            if not self.user.check_password(data['old_password']):
                raise forms.ValidationError("Incorrect old password")

            if data['new_password'] != data['password_confirm']:
                raise forms.ValidationError("New passwords must be same")

            return data

class AuthorizeForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'username', 'class': 'validate'}),
        required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'validate'}),
        required=True)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('No such user %s' % username)
        return username

    def clean_password(self):
        data = self.cleaned_data
        if 'username' in data and 'password' in data:
            password = self.cleaned_data['password']
            user = User.objects.get(username=self.cleaned_data['username'])
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            else:
                return password
