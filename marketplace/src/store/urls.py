from django.urls import path

from store.views import index, product_detail

urlpatterns = [
    path('', index, name='index'),
    path('product/<str:slug>/', product_detail, name='product'),
]