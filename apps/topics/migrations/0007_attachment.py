# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-18 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0006_auto_20180318_0035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='', upload_to='img')),
                ('file', models.FileField(default='', upload_to='file')),
                ('video', models.FileField(default='', upload_to='video')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('mtime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '附件上传',
                'verbose_name_plural': '附件上传',
            },
        ),
    ]
