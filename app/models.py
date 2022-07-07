from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Picture(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=255)
    image = models.ImageField(verbose_name='Изображение')
    owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='pictures')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'
