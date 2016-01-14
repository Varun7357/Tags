# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageboard', '0006_auto_20160112_0613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metafields',
            name='episodeNumber',
        ),
        migrations.AlterField(
            model_name='metafields',
            name='artist',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='metafields',
            name='contentType',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'KIRTAN', b'KIRTAN'), (b'KATHA', b'KATHA'), (b'PATH', b'PATH'), (b'TVSHOW', b'TVSHOW'), (b'LECTURE', b'LECTURE'), (b'MOVIES', b'MOVIES')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='metafields',
            name='duration',
            field=models.IntegerField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='metafields',
            name='fileTitle',
            field=models.CharField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='metafields',
            name='monetize',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
