# Generated by Django 5.1.1 on 2024-09-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videocourses', '0002_alter_video_preview_alter_video_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, upload_to='video/originals', verbose_name='Путь к видео'),
        ),
    ]
