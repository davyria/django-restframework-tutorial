# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='animals', verbose_name='Foto'),
        ),
    ]
