from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


# ViewSet可以使用router拼接
router = DefaultRouter()
router.register(r'^user', UserViewSet, basename='my_user')

urlpatterns = [
    path('', include(router.urls)),
    # path('register/', registration, name='register')
    
]
