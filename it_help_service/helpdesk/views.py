from django.http import HttpResponse


def index(request):
    # todo должна быть логика для новых отображения обращений (Админ видит все обращения, а обычный пользователь только свои)
    # todo добавить шаблон главной страницы
    return HttpResponse("Здесь будет отображаться список новых обращений")


def detail(request, order_id):
    # todo добавить шаблон для отображения деталей по заказу
    return HttpResponse(f"Детализация по задаче №{order_id}")


def orders(request):
    # todo добавить шаблон для отображения списка всех обращений
    return HttpResponse("Здесь будет отображаться список всех обращений")
