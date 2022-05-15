from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('product/<int:num1>/<int:num2>', views.product)

]