# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20150807_0400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='username',
            new_name='user',
        ),
    ]
