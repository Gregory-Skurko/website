from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(label='Your name', max_length=30)
    body = forms.Textarea()