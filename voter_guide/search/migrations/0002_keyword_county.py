# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-04 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='county',
            field=models.CharField(db_index=True, default='', max_length=100),
            preserve_default=False,
        ),
    ]