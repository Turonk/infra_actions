from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница')


def third_page(request):
    return HttpResponse('А это вторая страница')


def fourth_page(request):
    return HttpResponse('А это вторая страница')
