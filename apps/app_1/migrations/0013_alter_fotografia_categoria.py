# Generated by Django 5.1.7 on 2025-05-17 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0012_fotografia_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALÁXIA', 'Galáxia'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
    ]
