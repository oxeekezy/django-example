# Generated by Django 5.1.1 on 2024-09-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0004_products_large_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='large_description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Полное описание'),
        ),
    ]
