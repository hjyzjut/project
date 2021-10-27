from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OperateLogViewSet

# ViewSet可以使用router拼接
router = DefaultRouter()
router.register(r'^operate_log', OperateLogViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
