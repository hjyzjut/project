from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# ViewSet可以使用router拼接
router = DefaultRouter()
router.register(r'^gmv_budget', GmvBudgetViewSet)
router.register(r'^gmv_gsv_real', GmvGsvRealViewSet)
router.register(r'^gmv_week_real', GmvWeekRealViewSet)
router.register(r'^guaranteed_license_income', GuaranteedLicenseIncomeViewSet)
router.register(r'^real_license_income', RealLicenseIncomeViewSet)
router.register(r'^authorized_shop', AuthorizedShopViewSet)
router.register(r'^double_eleven', DoubleElevenViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
