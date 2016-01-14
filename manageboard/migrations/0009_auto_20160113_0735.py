# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageboard', '0008_auto_20160112_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='metafields',
            name='category',
            field=models.ForeignKey(choices=[(b'PEOPLE', b'PEOPLE'), (b'INSTITUTION', b'INSTITUTION'), (b'GOD', b'GOD'), (b'HOLYBOOK', b'HOLYBOOK'), (b'TOPICS', b'TOPICS')], to='manageboard.Category', max_length=200, blank=True, null=True),
            preserve_default=True,
        ),
    ]
