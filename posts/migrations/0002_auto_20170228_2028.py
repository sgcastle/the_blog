# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 20:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pud_date',
            new_name='pub_date',
        ),
    ]
