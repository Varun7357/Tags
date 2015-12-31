# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lam_user',
            name='media_source',
            field=models.CharField(default=datetime.datetime(2015, 12, 31, 8, 39, 57, 754625, tzinfo=utc), max_length=100, blank=True),
            preserve_default=False,
        ),
    ]
