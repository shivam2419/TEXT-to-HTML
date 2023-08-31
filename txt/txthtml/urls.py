from django.urls import path
from . import views

urlpatterns = [
    path('', views.convertor_view, name='convertor_view'),
    path('currency_convertion', views.cuurency_convertion, name='Currency_Converter'),
]