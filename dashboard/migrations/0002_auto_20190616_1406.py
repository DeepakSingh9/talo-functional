# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-16 08:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='High_School_degree',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='High_School_from',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='profile',
            name='High_School_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='High_School_till',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='profile',
            name='Junior_School_from',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='profile',
            name='Junior_School_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='Junior_School_till',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='profile',
            name='Junior_degree',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='bachelors_college_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='bachelors_degree',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='bachelors_education_from',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='profile',
            name='bachelors_education_till',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='profile',
            name='masters_college_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='masters_degree_name',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='masters_education_from',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='profile',
            name='masters_education_till',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
