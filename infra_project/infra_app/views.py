from django.http import HttpResponse


def index(request):
    return HttpResponse('ВСЕГО 6 Часов!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
