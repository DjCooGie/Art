# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-02 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20200203_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=40, null=True, unique=True),
        ),
    ]
