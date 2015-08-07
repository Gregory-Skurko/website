# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150807_0326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='username',
        ),
    ]
