from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator, name='pizza-dough'),
    path('table/', views.calculate, name='recipe-table'),
]
