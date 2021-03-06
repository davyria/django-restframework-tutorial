# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Raza')),
            ],
            options={
                'verbose_name': 'Raza',
                'verbose_name_plural': 'Razas',
            },
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Nacimiento')),
                ('gender', models.CharField(blank=True, choices=[('F', 'Hembra'), ('M', 'Macho')], max_length=1, null=True, verbose_name='Sexo')),
                ('color', models.CharField(blank=True, max_length=32, null=True, verbose_name='Color de pelo')),
                ('hair', models.CharField(blank=True, choices=[('S', 'Corto'), ('M', 'Semi-Largo'), ('L', 'Largo')], max_length=1, null=True, verbose_name='Longitud de pelo')),
                ('image', models.ImageField(upload_to='animals', verbose_name='Foto')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='cats.Breed', verbose_name='Raza')),
            ],
            options={
                'verbose_name': 'Gato',
                'verbose_name_plural': 'Gatos',
            },
        ),
    ]
