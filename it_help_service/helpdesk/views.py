from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Orders


def index(request):
    # todo должна быть логика для новых отображения обращений (Админ видит все обращения, а обычный пользователь только свои)
    # todo добавить стилей в шаблон index.html
    orders = Orders.objects.filter(status='new').order_by('create_date')
    context = {
        'orders': orders
    }
    return render(request, 'helpdesk/index.html', context)


def detail(request, order_id):
    # todo добавить стилей в шаблон order.html
    order = get_object_or_404(Orders, pk=order_id)
    return render(request, 'helpdesk/order.html', {'order': order})


def orders(request):
    # todo добавить стилей в шаблон orders.html
    orders = Orders.objects.all()
    return render(request, 'helpdesk/orders.html', {'orders': orders})
