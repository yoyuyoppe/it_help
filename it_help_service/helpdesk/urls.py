from django.urls import path

from . import views
# добавим пространство имен
app_name = 'helpdesk'
urlpatterns = [
    # /helpdesk/
    path('', views.index, name='index'),
    # /helpdesk/orders
    path('orders/', views.orders, name='orders'),
    # /helpdesk/orders/order/1
    path('orders/order/<int:order_id>/', views.detail, name='detail'),
]
