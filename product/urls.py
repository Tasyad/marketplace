from django.urls import path, include
from .views import ProductListAPIView, GetCartAPIView


urlpatterns = [
    path('', ProductListAPIView.as_view(), name='list'),
    path('cart/<int:id>', GetCartAPIView.as_view(), name='cart'),
]