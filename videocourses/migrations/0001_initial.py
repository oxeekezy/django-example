# Generated by Django 5.1.1 on 2024-09-18 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True, verbose_name='URL')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='merch/images', verbose_name='Путь к превью')),
                ('video', models.ImageField(blank=True, upload_to='merch/images', verbose_name='Путь к видео')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
                'db_table': 'video',
            },
        ),
    ]
