from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from hlsh_report.utils.reportViewSet import ReportViewSet
from rest_framework.permissions import *
from rest_framework.decorators import *
from hlsh_report.utils.response import BaseResponse
from django.shortcuts import get_object_or_404
from hlsh_report.apps.logs.models import OperateLog
import datetime
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
    search_fields = ['id']
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



class AuthorizedShopViewSet(ReportViewSet):
    permission_classes = [IsAuthenticated]

    queryset = AuthorizedShop.objects.all()
    serializer_class = AuthorizedShopSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['id', 'bussiness']
    filterset_fields = ['id']
    ordering_fields = ['update_time', 'create_time']

    # 只允许POST,GET请求
    http_method_names = ['get', 'post', 'patch', 'put']

    @action(methods=['put'], detail=False)
    def multiple_update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instances = []  # 这个变量是用于保存修改过后的对象，返回给前端
        print(request.data)
        for item in request.data:  # 遍历列表中的每个对象字典
            instance = get_object_or_404(AuthorizedShop, id=int(item['id']))  # 通过ORM查找实例
            # 构造序列化对象，注意partial=True表示允许局部更新
            # 由于我们前面重写了get_serializer方法，进行了many=True的判断。
            # 但此处不需要many=True的判断，所以必须调用父类的get_serializer方法
            serializer = super().get_serializer(instance, data=item, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            instances.append(serializer.data)  # 将数据添加到列表中
        operate_log = OperateLog.objects.create(user=request.user, operate_type='更新',
                                                data_model='授权开店清单',
                                                file_name='-',
                                                operate_time=datetime.datetime.now())
        return BaseResponse(data=instances, code=200, msg="更新成功", success=True, status=status.HTTP_200_OK)



class DoubleElevenViewSet(ReportViewSet):
    
    permission_classes = [IsAuthenticated]

    queryset = DoubleEleven.objects.all()
    serializer_class = DoubleElevenSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['id']
    filterset_fields = ['id']
    ordering_fields = ['update_time', 'create_time']

    # 只允许POST,GET请求
    http_method_names = ['get','post']
    

class WeeklySalesReportViewSet(ReportViewSet):
    
    permission_classes = [IsAuthenticated]

    queryset = WeeklySalesReport.objects.all()
    serializer_class = WeeklySalesReportSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['id']
    filterset_fields = ['id']
    ordering_fields = ['update_time', 'create_time']

    # 只允许POST,GET请求
    http_method_names = ['get','post']