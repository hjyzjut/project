from re import search
from rest_framework import serializers
from .models import *
from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from hlsh_report.utils.reportViewSet import ReportViewSet
from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework_simplejwt import authentication
# Create your views here.

class GmvBudgetViewSet(ReportViewSet):
    permission_classes = [IsAuthenticated]
   
    # GMV预算的视图

    queryset = GmvBudget.objects.all()
    serializer_class = GmvBudgetSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['id','bussiness']
    filterset_fields = ['id']
    ordering_fields = ['update_time', 'create_time']

    # 只允许POST,GET请求
    # http_method_names = ['get','post']

    # permission_classes_by_action = {'create': [AllowAny],
    #                                 'list': [IsAuthenticated],
    #                                 'update': [IsAuthenticated],
    #                                 'retrieve': [AllowAny],
    #                                 'destroy': [IsAuthenticated]
    #                                 }
    # authentication_classes = ([])

    # 根据action获取权限
    # def get_permissions(self):
    #     print(self.action)
    #     try:
    #         return [permissions() for permissions in self.permission_classes_by_action[self.action]]
    #     except KeyError:
    #         return [permissions() for permissions in self.permission_classes]

    # def get_authenticators(self):
    #     # print('username{}'.format(self.request.user))
    #     print(self.authentication_classes)
    #     """
    #     Instantiates and returns the list of authenticators that this view can use.
    #     """
    #     if self.request.method in ('POST'):
    #         self.authentication_classes = ([])
        

    #     return [auth() for auth in self.authentication_classes]

class GmvGsvRealViewSet(ReportViewSet):

    permission_classes = [IsAuthenticated]

    queryset = GmvGsvReal.objects.all()
    serializer_class = GmvGsvRealSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['id','bussiness']
    filterset_fields = ['id']
    ordering_fields = ['update_time', 'create_time']
    
    # 只允许POST,GET请求
    http_method_names = ['get','post']

class GmvWeekRealViewSet(ReportViewSet):

    permission_classes = [IsAuthenticated]

    queryset = GmvWeekReal.objects.all()
    serializer_class = GmvWeekRealSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['id','bussiness']
    filterset_fields = ['id']
    ordering_fields = ['update_time', 'create_time']


    # 只允许POST,GET请求
    http_method_names = ['get','post']


class GuaranteedLicenseIncomeViewSet(ReportViewSet):

    permission_classes = [IsAuthenticated]

    queryset = GuaranteedLicenseIncome.objects.all()
    serializer_class = GuaranteedLicenseIncomeSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['id','bussiness']
    filterset_fields = ['id']
    ordering_fields = ['update_time', 'create_time']

    # 只允许POST,GET请求
    http_method_names = ['get','post']


class RealLicenseIncomeViewSet(ReportViewSet):

    permission_classes = [IsAuthenticated]
    
    queryset = RealLicenseIncome.objects.all()
    serializer_class = RealLicenseIncomeSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['id','bussiness']
    filterset_fields = ['id']
    ordering_fields = ['update_time', 'create_time']

    # 只允许POST,GET请求
    http_method_names = ['get','post']