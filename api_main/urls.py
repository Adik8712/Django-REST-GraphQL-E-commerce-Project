from .views import CategoryViewSet, ProductViewSet
from django.urls import path
from rest_framework import routers  

router = routers.DefaultRouter()

router.register('api/category', CategoryViewSet, basename='Category')
router.register('api/product', ProductViewSet, basename='Product')


urlpatterns = []
urlpatterns += router.urls