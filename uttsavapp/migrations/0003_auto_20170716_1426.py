# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-16 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uttsavapp', '0002_auto_20170716_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendordetailtable',
            name='event_category',
        ),
        migrations.RemoveField(
            model_name='vendordetailtable',
            name='vending_category',
        ),
        migrations.AddField(
            model_name='vendordetailtable',
            name='EventCategory',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='vendordetailtable',
            name='VendingCategory',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='eventcategoryct',
            name='event_code',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='vendingcategoryct',
            name='vending_code',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='vendorlisttable',
            name='EventCategory',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='vendorlisttable',
            name='VendingCategory',
            field=models.IntegerField(default=None),
        ),
    ]
