# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'blog', '0001_initial'), (b'blog', '0002_tag'), (b'blog', '0003_auto_20150806_0057'), (b'blog', '0004_tag'), (b'blog', '0005_post_tag'), (b'blog', '0006_auto_20150806_0112'), (b'blog', '0007_auto_20150806_0114'), (b'blog', '0008_avatar'), (b'blog', '0009_auto_20150806_1807'), (b'blog', '0010_auto_20150807_0213'), (b'blog', '0011_auto_20150807_0213'), (b'blog', '0012_auto_20150807_0217'), (b'blog', '0013_auto_20150807_0217'), (b'blog', '0014_auto_20150807_0217'), (b'blog', '0015_auto_20150807_0217'), (b'blog', '0016_auto_20150807_0218'), (b'blog', '0017_auto_20150807_0222'), (b'blog', '0018_auto_20150807_0255'), (b'blog', '0019_auto_20150807_0255'), (b'blog', '0020_remove_post_username'), (b'blog', '0021_auto_20150807_0258'), (b'blog', '0022_remove_post_author'), (b'blog', '0023_post_author'), (b'blog', '0024_auto_20150807_0305'), (b'blog', '0025_auto_20150807_0306'), (b'blog', '0026_auto_20150807_0307'), (b'blog', '0027_remove_post_author'), (b'blog', '0028_auto_20150807_0308'), (b'blog', '0029_auto_20150807_0309'), (b'blog', '0030_auto_20150807_0309')]

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.OneToOneField(to='blog.Post'),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag', models.CharField(max_length=20, serialize=False, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to=b'blog.Tag', blank=True),
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('img', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=30),
        ),
    ]
