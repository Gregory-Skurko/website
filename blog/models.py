from django.db import models
from django.contrib.auth.models import User
# Create your models here.
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

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.OneToOneField(Post)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.author

    def __unicode__(self):
        return self.author


class Avatar(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    img = models.ImageField()

    def __str__(self):
        return self.img.name

    def __unicode__(self):
        return self.img.name


























