from django.urls import path

from . import views

app_name = 'infra_app'

urlpatterns = [
    path('/', views.index, name='index'),
    path('/second_page/', views.second_page, name='second_page'),

]
