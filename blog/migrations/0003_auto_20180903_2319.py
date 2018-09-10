# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-03 14:19
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180903_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='d', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='Inglat',
            field=models.CharField(blank=True, help_text='위도/경도 포맷으로 입력', max_length=50, validators=[blog.models.lnglat_validator]),
        ),
    ]