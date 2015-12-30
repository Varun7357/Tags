# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lam_user',
            name='install_count',
            field=models.IntegerField(default=0, max_length=100),
            preserve_default=True,
        ),
    ]
