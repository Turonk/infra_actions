from django.http import HttpResponse


def index(request):
    return HttpResponse('Давай workflow! Работай!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
