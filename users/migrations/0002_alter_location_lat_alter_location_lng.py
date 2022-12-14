# Generated by Django 4.1.1 on 2022-10-07 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=10, max_digits=15, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.DecimalField(decimal_places=10, max_digits=15, null=True, verbose_name='Долгота'),
        ),
    ]
