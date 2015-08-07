# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20150807_0255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='username',
        ),
    ]
