from django.urls import path

from . import views


app_name = 'minerals'
urlpatterns = [
    path('', views.mineral_list, name='list'),
    path('details/<pk>/', views.mineral_details, name='details'),
]