from django.urls import path

from . import views

urlpatterns = [
    # /helpdesk/
    path('', views.index, name='index'),
    # /helpdesk/orders
    path('orders/', views.orders, name='orders'),
    # /helpdesk/orders/1
    path('orders/<int:order_id>/', views.detail, name='detail'),
]
