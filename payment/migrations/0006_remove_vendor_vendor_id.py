# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 18:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_vendor_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='vendor_id',
        ),
    ]