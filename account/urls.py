from django.urls import path

from product.views import GetCartAPIView
from .views import (
    RegisterApiView
)


urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
]

