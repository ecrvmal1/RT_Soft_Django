from django.db import models


class Category(models.Model):
    """
    Модель категории
    Содержит в себе поля:
    name - название категории
    """

    name = models.CharField(max_length=128, unique=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Record(models.Model):
    """
    Модель
    Содержит в себе поля:
    file_url - ссылка на изображение
    num_of_show - number of times
    category - категория ссылки
    """

    file_url = models.CharField(max_length=128, unique=True)
    num_of_show = models.PositiveIntegerField(default=0)
    category = models.ManyToManyField(Category, related_name="records")

    objects = models.Manager()

    # def __str__(self):
    #     return self.file_url, self.num_of_show, self.category

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"

