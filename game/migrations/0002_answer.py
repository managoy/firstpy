# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 02:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=255)),
                ('q', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.question')),
            ],
        ),
    ]
