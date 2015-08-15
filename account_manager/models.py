import os
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver

AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='img/avatars/', blank=True)

# These two auto-delete files from filesystem when they are unneeded:
@receiver(models.signals.post_delete, sender=User)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.avatar:
        if os.path.isfile(instance.avatar.path):
            os.remove(instance.avatar.path)

@receiver(models.signals.pre_save, sender=User)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is changed.
    """
    if not instance.pk:
        return False

    try:
        old_file = User.objects.get(pk=instance.pk).avatar
    except User.DoesNotExist:
        return False

    new_file = instance.avatar
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)