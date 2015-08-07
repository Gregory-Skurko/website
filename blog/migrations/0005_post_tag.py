# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(blank=True, to='blog.Tag', null=True),
        ),
    ]
