# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0020_user_generate_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_generate_list',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user_generate_list',
            name='recommend',
            field=models.NullBooleanField(db_index=True),
        ),
    ]