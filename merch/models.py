from django.db import models


class Categories(models.Model):
    name = models.CharField(
        max_length=150, unique=True, verbose_name="Наименование категории"
    )
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="URL")

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    name = models.CharField(
        max_length=150, unique=True, verbose_name="Наименование продукции"
    )
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="URL")
    description = models.TextField(
        max_length=500, blank=True, null=True, verbose_name="Краткое описание"
    )

    large_description = models.TextField(
        max_length=1000, blank=True, null=True, verbose_name="Полное описание"
    )

    image = models.ImageField(
        upload_to="merch/images",
        blank=True,
        null=True,
        verbose_name="Изображение",
    )
    price = models.DecimalField(
        default=0.00, max_digits=15, decimal_places=2, verbose_name="Цена"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Скидка в процентах"
    )
    count = models.PositiveBigIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(
        to=Categories, on_delete=models.PROTECT, verbose_name="Категория"
    )

    class Meta:
        db_table = "product"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self) -> str:
        return f"{self.name} ({self.count} шт.)"

    def display_id(self):
        return f"{self.id:07}"

    def final_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)

        return self.price
