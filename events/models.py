from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Event(models.Model):
    title = models.CharField(
        'Название',
        max_length=200,
    )
    description = models.TextField(
        'Описание',
        blank=True,
    )
    date = models.DateField(
        'Дата',
    )

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Создатель',
    )

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return f'{self.title}: {self.date}'
