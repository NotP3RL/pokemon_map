# Generated by Django 3.1.14 on 2022-11-18 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0017_auto_20221118_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
    ]
