# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0010_auto_20170730_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='image',
            field=models.ImageField(blank=True, default='img/itugnu.png', upload_to='uploaded'),
        ),
    ]
