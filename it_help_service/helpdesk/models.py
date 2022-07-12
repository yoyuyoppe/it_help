from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import mimetypes
from .validators import validate_file_extension


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


def attachment_path(instance, filename):
    return instance.attachment_path(filename)


class Attachment(models.Model):
    """
    Представляет файл, прикрепленный к последующему действию.
    Это может быть вложение в электронном письме или загрузка через веб-интерфейс.
    """

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'
        db_table = 'attachments'

    order = models.ForeignKey(
        Orders,
        on_delete=models.CASCADE,
        verbose_name='Обращение'
    )

    file = models.BinaryField()

    filename = models.CharField(
        blank=True,
        max_length=1000,
        validators=[validate_file_extension]
    )

    mime_type = models.CharField(
        blank=True,
        max_length=255,
    )

    size = models.IntegerField(
        blank=True,
        help_text='Размер файла в байтах',
    )

    def __str__(self):
        return '%s' % self.filename

    def save(self, *args, **kwargs):

        if not self.size:
            self.size = self.get_size()

        if not self.filename:
            self.filename = self.get_filename()

        if not self.mime_type:
            self.mime_type = \
                mimetypes.guess_type(self.filename, strict=False)[0] or \
                'application/octet-stream'

        return super.save(*args, **kwargs)

    def get_filename(self):
        return str(self.file)

    def get_size(self):
        return self.file.file.size

