# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('client_id', models.EmailField(validators=[django.core.validators.EmailValidator()], unique=True, max_length=254)),
                ('configured_url', models.TextField(validators=[django.core.validators.URLValidator()], max_length=2000)),
                ('is_active', models.BooleanField(default=True)),
                ('configured_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
