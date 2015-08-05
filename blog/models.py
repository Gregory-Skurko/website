from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.author

    def __unicode__(self):
        return self.author
