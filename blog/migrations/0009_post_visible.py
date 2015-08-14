# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150813_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
