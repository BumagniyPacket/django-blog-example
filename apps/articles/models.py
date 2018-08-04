from ckeditor.fields import RichTextField
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from filer.fields.image import FilerImageField

from apps.common.mixins import GenerateSlugMixin
from .managers import ArticleManager


class Article(GenerateSlugMixin, models.Model):
    class Meta:
        verbose_name = 'Блог - пост'
        verbose_name_plural = 'Блог - посты'

        ordering = ['-timestamp', '-updated']

    objects = ArticleManager()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1,
        verbose_name='Пользователь'
    )
    title = models.CharField(
        max_length=120,
        verbose_name='Заголовок поста'
    )
    image = FilerImageField(
        blank=False, null=True,
        verbose_name='Изображение',
    )
    description = models.TextField(
        max_length=400,
        verbose_name='Описание поста'
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        verbose_name='Слаг',
    )
    content = RichTextField(verbose_name='Контент')
    draft = models.BooleanField(
        default=False,
        verbose_name='В процессе написания'
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Обновлен'
    )
    views = models.IntegerField(
        default=0,
        verbose_name='Просмотров'
    )
    category = models.ForeignKey(
        'categories.Category',
        related_name='articles',
        verbose_name='Категория',
        on_delete=models.CASCADE,
        blank=False
    )
    tags = models.ManyToManyField(
        'tags.Tag',
        related_name='articles',
        blank=False,
    )

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        return reverse(
            'frontend-blog:blog-article-detail',
            kwargs={'pk': self.pk}
        )

    def add_view(self):
        self.views += 1
        self.save()

    def get_views(self):
        views = self.views
        return views
