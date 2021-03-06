# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='meta',
            name='status',
            field=models.ForeignKey(to='manageboard.MetaStatus', max_length=20, null=True),
            preserve_default=True,
        ),
    ]
