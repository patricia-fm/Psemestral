# Generated by Django 3.1.3 on 2020-11-12 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.URLField(max_length=210, verbose_name='Url de la Imagen'),
        ),
    ]
