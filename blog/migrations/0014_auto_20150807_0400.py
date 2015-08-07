# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20150807_0358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='username',
            new_name='user',
        ),
    ]
