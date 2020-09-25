from django.db import models


class Post(models.Model):
    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = '-created_at',

    author = models.CharField('автор', max_length=50)
    text = models.TextField('текст')
    created_at = models.DateTimeField('дата публикации', auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.author} - {self.text[:50]}'
