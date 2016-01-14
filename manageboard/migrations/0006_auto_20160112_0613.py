# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('manageboard', '0005_auto_20151223_1847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metafields',
            old_name='book',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='metafields',
            name='god',
        ),
        migrations.RemoveField(
            model_name='metafields',
            name='shrines',
        ),
        migrations.RemoveField(
            model_name='metafields',
            name='topic',
        ),
        migrations.AddField(
            model_name='metafields',
            name='create_dt',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 12, 6, 13, 35, 640896, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metafields',
            name='entity',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metafields',
            name='login_required',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metafields',
            name='monetize',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metafields',
            name='premium_required',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metafields',
            name='tags',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='metafields',
            name='themes',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'HINDUISM', b'HINDUISM'), (b'ISLAM', b'ISLAM'), (b'SIKH', b'SIKH'), (b'CHRISTIANITY', b'CHRISTIANITY'), (b'YOGA', b'YOGA'), (b'MEDITATION', b'MEDITATION'), (b'SPIRITUALITY', b'SPIRITUALITY')]),
            preserve_default=True,
        ),
    ]
