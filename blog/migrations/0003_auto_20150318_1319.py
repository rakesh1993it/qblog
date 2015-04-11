# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150316_0045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name': 'Blog Entry', 'verbose_name_plural': 'Blog Entries', 'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='entry',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
