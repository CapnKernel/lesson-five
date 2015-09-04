# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_create_fk_to_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='start',
            field=models.DateTimeField(help_text='Format: 2006-10-25 14:30', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='entry',
            name='stop',
            field=models.DateTimeField(null=True, help_text='Format: 2006-10-25 14:30', blank=True),
        ),
    ]
