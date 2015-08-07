# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150806_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.OneToOneField(to='blog.Post'),
        ),
    ]
