import uuid

from django.contrib.auth import get_user_model
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

User = get_user_model()


class Post(MPTTModel):
    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = '-created_at',

    class MPTTMeta:
        order_insertion_by = ['-created_at']

    id = models.UUIDField(verbose_name='идентификатор', primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор', max_length=50, db_index=True)
    body = models.TextField('содержание поста')
    created_at = models.DateTimeField('дата публикации', auto_now_add=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='children',
                            verbose_name='родительский пост', null=True, blank=True, db_index=True)

    def __str__(self) -> str:
        return f'{self.created_at} | {self.author} | {self.body[:50]}'
