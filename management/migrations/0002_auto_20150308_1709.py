# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='unit',
            field=models.CharField(max_length=200, default='Meters'),
            preserve_default=True,
        ),
    ]
