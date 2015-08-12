from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False

class User(AbstractUser):
    avatar = models.ImageField(upload_to='static/img/avatars/', blank=True)

class Tag(models.Model):
    tag = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.tag

    def __unicode__(self):
        return self.tag

class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, blank=True)
    body = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.OneToOneField(Post)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.author

    def __unicode__(self):
        return self.author






























