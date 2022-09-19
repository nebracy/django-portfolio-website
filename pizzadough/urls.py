from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator, name='pizza-dough'),
    path('calculate/', views.calculate, name='calculate-table'),
]
