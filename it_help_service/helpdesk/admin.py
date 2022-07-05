from django.contrib import admin
from .models import Orders


class OrdersAdmin(admin.ModelAdmin):
    # задаём методы для получения полей из связанных таблицы
    def username(self, obj):
        return obj.author.username

    # задаем краткое наименование для полученного поля выше
    username.short_description = 'Автор'

    # поля для отображения
    list_display = ('id', 'theme', 'username', 'create_date', 'edit_date', 'status')

    # поля для поиска
    search_fields = ('id', 'author__username', 'author__email', 'theme')

    # поля для замены выпадашки
    raw_id_fields = ('author', )


admin.site.register(Orders, OrdersAdmin)
