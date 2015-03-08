# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_entered', models.DateTimeField(auto_now_add=True, verbose_name='Date Entered')),
                ('description', models.CharField(max_length=800)),
                ('total', models.DecimalField(max_digits=6, decimal_places=2)),
                ('materials', models.ManyToManyField(to='materials.Material')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
