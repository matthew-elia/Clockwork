# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clockwork', '0002_auto_20160811_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]
