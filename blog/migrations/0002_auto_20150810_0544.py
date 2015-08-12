# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to=b'avatars/', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=254, verbose_name='email address'),
        ),
    ]
