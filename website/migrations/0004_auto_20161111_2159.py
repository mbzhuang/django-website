# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 21:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_topmovies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topmovies',
            old_name='genre',
            new_name='Genre',
        ),
        migrations.RenameField(
            model_name='topmovies',
            old_name='poster',
            new_name='Poster',
        ),
        migrations.RenameField(
            model_name='topmovies',
            old_name='created',
            new_name='Released',
        ),
        migrations.RenameField(
            model_name='topmovies',
            old_name='year',
            new_name='Year',
        ),
    ]