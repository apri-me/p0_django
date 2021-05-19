from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('second/', views.second_view, name='second'),
]
