# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20141112_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='publicado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
