# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageboard', '0004_auto_20151218_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='metafields',
            name='artist',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metafields',
            name='book',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metafields',
            name='contentType',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'KIRTAN', b'KIRTAN'), (b'KATHA', b'KATHA'), (b'PATH', b'PATH'), (b'TVSHOW', b'TVSHOW')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metafields',
            name='description',
            field=models.CharField(max_length=600, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metafields',
            name='duration',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metafields',
            name='episodeNumber',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metafields',
            name='fileTitle',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metafields',
            name='god',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metafields',
            name='language',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metafields',
            name='seriesNumber',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metafields',
            name='seriesTitle',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metafields',
            name='shrines',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metafields',
            name='themes',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metafields',
            name='topic',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='metafields',
            name='mediaType',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'AUDIO', b'AUDIO'), (b'VIDEO', b'VIDEO')]),
            preserve_default=True,
        ),
    ]
