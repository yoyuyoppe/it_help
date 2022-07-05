from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Orders(models.Model):
    """Класс для описания заявки"""

    class Meta:
        db_table = 'orders'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    statuses = (('new', 'Новая'),
                ('read', 'Прочитана'))

    author = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name="Автор")
    theme = models.CharField(verbose_name="Тема", max_length=250)
    content = models.TextField(verbose_name="Текст", null=True)
    create_date = models.DateTimeField(verbose_name="Создано", auto_now_add=True)
    edit_date = models.DateTimeField(verbose_name="Изменено", blank=True, null=True)
    status = models.CharField(verbose_name='Статус', max_length=25, choices=statuses, null=True)

    def __str__(self):
        return f'Заявка №{self.id} на тему "{self.theme}" от {self.author.username}'

    def save(self, *args, **kwargs):
        self.edit_date = datetime.now()
        super().save(self, *args, **kwargs)
