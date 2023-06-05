from django.urls import path
from . import views

urlpatterns =[
    path('stock_list/',views.stock_fetch,name ='stock_list'),
    path('buy_stock/',views.buy_stock,name='buy_stock'),


]