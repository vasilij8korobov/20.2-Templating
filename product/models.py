from django.db import models
from users.models import User

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Категория",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание категории", **NULLABLE
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}\n {self.description}"


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Продукт",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание товара", **NULLABLE
    )
    photo = models.ImageField(
        upload_to="product/image/",
        verbose_name="Фото",
        help_text="Загрузите фото продукта",
        **NULLABLE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        **NULLABLE,
        related_name="products",
    )
    purchase_price = models.IntegerField(
        verbose_name="Цена", help_text="Введите цену за покупку"
    )
    creation_date = models.DateField(
        verbose_name="Дата создания",
        help_text="Введите дату создания",
        auto_now_add=True,
    )
    last_modified_date = models.DateField(
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
        auto_now=True,
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        help_text="Владелец продукта",
        **NULLABLE,
    )

    def set_current_version(self, version):
        # Сбросить все текущие версии
        self.versions.update(status_version=False)
        # Установить новую текущую версию
        version.status_version = True
        version.save()

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]

    def __str__(self):
        return f"{self.name}\n {self.description}\n {self.photo}\n {self.category}\n {self.purchase_price}\n {self.creation_date}\n {self.last_modified_date}"


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name="versions",
        verbose_name="Продукт",
    )
    num_version = models.IntegerField(
        **NULLABLE, verbose_name="Номер версии", help_text="Введите номер версии"
    )
    name_version = models.CharField(
        max_length=100,
        verbose_name="Наименование версии",
        help_text="Укажите название версии",
    )
    status_version = models.BooleanField(
        default=False,
        verbose_name="Статус версии",
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["product", "num_version"]

    def __str__(self):
        return f"{self.product} - {self.name_version} (Версия {self.num_version})"
