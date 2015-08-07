# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_aauthor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='aauthor',
        ),
    ]
