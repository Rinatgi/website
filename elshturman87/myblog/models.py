from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    "Категории"
    name = models.CharField("Категория", max_length=150)
    description = models.CharField("Описание", max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Post(models.Model):
    "Пост"
    title = models.CharField("Заголовок записи", max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Текст записи")
    image = models.ImageField("Изображение", upload_to="images/")
    url = models.SlugField(max_length=250, unique_for_date='publish_date')
    publish_date = models.DateField("Дата публикации", default=datetime.now)
    update_date = models.DateField("Дата обновления", auto_now=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f'{self.title} {self.author}'


