# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageboard', '0002_auto_20151214_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meta',
            name='link',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
