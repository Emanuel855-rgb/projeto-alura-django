# Generated by Django 5.1.7 on 2025-04-08 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0003_fotografia_publicado'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data_puclicacao',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
