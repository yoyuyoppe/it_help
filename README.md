# it_help_service
Create project:
django-admin startproject it_help_service

Create app: django-admin startapp helpdesk

Run server:  python manage.py runserver

Migrate: python manage.py migrate - команда migrate просматривает настройку INSTALLED_APPS и создает все необходимые таблицы базы данных в соответствии с настройками базы данных в вашем файле mysite/settings.py и миграциями базы данных, поставляемыми с приложением (мы рассмотрим их позже).

$ python manage.py makemigrations helpdesk - выполнить после создания моделей и добавления  приложения в INSTALLED_APP

$ python manage.py sqlmigrate helpdesk 0001 - выводит sql скрипт, который будет использоваться при миграции


