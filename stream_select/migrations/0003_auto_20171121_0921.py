# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 09:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream_select', '0002_auto_20171119_2221'),
    ]

    operations = [
        migrations.DeleteModel(
            name='info',
        ),
        migrations.DeleteModel(
            name='result',
        ),
    ]
