# Generated by Django 5.1.7 on 2025-05-22 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0014_alter_fotografia_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.ImageField(blank=True, storage='storages.backends.s3boto3.S3Boto3Storage', upload_to='%Y/%m/%d'),
        ),
    ]
