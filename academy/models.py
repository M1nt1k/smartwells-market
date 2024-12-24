from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from taggit.managers import TaggableManager
from taggit.models import GenericTaggedItemBase, TagBase


class ItemTag(TagBase):
    image = models.ImageField(
        upload_to='categories/',
        verbose_name='Изображение',
        blank=True
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
        )

    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")


class TaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(
        ItemTag,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name='Категория',
    )


class Item(models.Model):
    BASE_EDUCATION_CHOICES = [
        ('SPO', 'Среднее профессиональное образование'),
        ('VO', 'Высшее образование'),
    ]

    title = models.CharField(max_length=200, verbose_name='Название',)
    description = models.TextField(verbose_name='Описание',)
    slug = models.CharField(
        unique=True,
        max_length=50,
    )
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления',)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Новая цена',
    )
    old_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Старая цена',
        blank=True,
        null=True,
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='items/',
        blank=True,
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name='Доступно',
    )
    base_education = models.CharField(
        max_length=3,
        choices=BASE_EDUCATION_CHOICES,
        default='VO',
        verbose_name="Образование на базе"
    )
    duration = models.CharField(
        max_length=100,
        default='100',
        verbose_name='Срок обучения',
    )
    tags = TaggableManager(through=TaggedItem, related_name="tagged_items", verbose_name='Категории',)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-price']
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'

