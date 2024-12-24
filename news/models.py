from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200)  # Заголовок
    slug = models.SlugField(unique=True, blank=True)  # URL-адрес статьи
    content = models.TextField()  # Текст статьи
    published_date = models.DateTimeField(auto_now_add=True)  # Дата публикации
    author = models.CharField(max_length=100)  # Автор статьи
    image = models.ImageField(upload_to='articles/', blank=True, null=True)  # Изображение

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news:article_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title