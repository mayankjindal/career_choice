# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 22:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream_select', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='result',
            name='stream1',
        ),
        migrations.RemoveField(
            model_name='result',
            name='stream2',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
