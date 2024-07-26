from django.urls import path
from . import views

app_name = 'estore'

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.view_cart, name='view_cart'),
    path('home/', views.home, name='home'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]
