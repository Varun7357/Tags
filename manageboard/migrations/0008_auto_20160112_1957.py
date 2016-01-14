# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageboard', '0007_auto_20160112_0750'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Themes',
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
            name='contentType',
            field=models.ForeignKey(choices=[(b'KIRTAN', b'KIRTAN'), (b'KATHA', b'KATHA'), (b'PATH', b'PATH'), (b'TVSHOW', b'TVSHOW'), (b'LECTURE', b'LECTURE'), (b'MOVIES', b'MOVIES')], to='manageboard.ContentType', max_length=200, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='metafields',
            name='mediaType',
            field=models.ForeignKey(choices=[(b'AUDIO', b'AUDIO'), (b'VIDEO', b'VIDEO')], to='manageboard.MediaType', max_length=100, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='metafields',
            name='themes',
            field=models.ForeignKey(choices=[(b'HINDUISM', b'HINDUISM'), (b'ISLAM', b'ISLAM'), (b'SIKH', b'SIKH'), (b'CHRISTIANITY', b'CHRISTIANITY'), (b'YOGA', b'YOGA'), (b'MEDITATION', b'MEDITATION'), (b'SPIRITUALITY', b'SPIRITUALITY')], to='manageboard.Themes', max_length=200, blank=True, null=True),
            preserve_default=True,
        ),
    ]
