# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170118_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='state',
            field=models.CharField(choices=[('w1', 'w1'), ('g1', 'g1'), ('w2', 'w2'), ('g2', 'g2'), ('w3', 'w3'), ('g31', 'g31'), ('g32', 'g32'), ('g33', 'g33')], default='w1', max_length=20),
        ),
        migrations.AlterField(
            model_name='userstate',
            name='state',
            field=models.CharField(choices=[('s1', 's1'), ('t1', 't1'), ('w1', 'w1'), ('g1', 'g1'), ('g2', 'g2'), ('s2', 's2'), ('t2', 't2'), ('w3', 'w3'), ('s3', 's3'), ('t3', 't3'), ('g31', 'g31'), ('g32', 'g32'), ('g33', 'g33')], default='s1', max_length=20),
        ),
    ]
