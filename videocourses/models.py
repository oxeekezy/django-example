from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="URL")
    preview = models.ImageField(
        upload_to="video/previews",
        blank=True,
        null=True,
        verbose_name="Путь к превью",
    )
    video = models.FileField(
        upload_to="video/originals",
        blank=True,
        null=False,
        verbose_name="Путь к видео",
    )

    class Meta:
        db_table = "video"
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def __str__(self) -> str:
        return self.name
