# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-07 08:34
from __future__ import unicode_literals

from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Ad = apps.get_model("ads", "Ad")
    AdImage = apps.get_model("ads", "AdImage")
    for ad in Ad.objects.all():
        AdImage.objects.create(
            device='sm',
            image=ad.image)


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_adimage'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
