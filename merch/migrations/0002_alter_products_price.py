# Generated by Django 4.2.8 on 2024-09-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name='Цена'),
        ),
    ]
