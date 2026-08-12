from django.urls import path, include
from catalog.views import ProductView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', ProductView, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
