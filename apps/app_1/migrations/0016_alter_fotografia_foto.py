# Generated by Django 5.1.7 on 2025-05-22 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0015_alter_fotografia_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.ImageField(blank=True, upload_to='%Y/%m/%d'),
        ),
    ]
