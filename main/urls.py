from django.urls import path
from .views import IndexView, ProductDetailView

urlpatterns = [
    path('', IndexView, name='index'),
    path('product/<slug:slug>/', ProductDetailView, name='product_detail'),
]
