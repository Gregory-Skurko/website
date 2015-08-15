from django.db import models
from account_manager.models import User

class Tag(models.Model):
    tag = models.CharField(max_length=30)

    def __str__(self):
        return self.tag

    def __unicode__(self):
        return self.tag

class Post(models.Model):
    user = models.ForeignKey(User, related_name='post_user')
    visible = models.BooleanField(default=True)

    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    rating = models.IntegerField(default=0)

    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comment_user')
    post = models.ForeignKey(Post)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    voice = models.ManyToManyField(User, related_name='comment_voice')
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.author

    def __unicode__(self):
        return self.author

class Rating(models.Model):
    value = models.BooleanField()
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post, related_name='rating_post')





























