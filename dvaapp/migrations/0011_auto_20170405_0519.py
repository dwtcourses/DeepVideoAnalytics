# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 05:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0010_auto_20170404_1628'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExternalDataset',
        ),
        migrations.AddField(
            model_name='vdndataset',
            name='aws_bucket',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vdndataset',
            name='aws_key',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vdndataset',
            name='aws_region',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vdndataset',
            name='aws_requester_pays',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vdndataset',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vdndataset',
            name='date_imported',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vdndataset',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vdndataset',
            name='download_url',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vdndataset',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vdndataset',
            name='response',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vdndataset',
            name='url',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vdndataset',
            name='youtube_video',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vdndataset',
            name='child_video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
    ]
