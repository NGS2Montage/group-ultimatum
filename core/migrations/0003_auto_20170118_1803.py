# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170118_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstate',
            name='state',
            field=models.CharField(choices=[('s1', 's1'), ('t1', 't1'), ('w1', 'w1'), ('g1', 'g1')], default='s1', max_length=20),
        ),
    ]
