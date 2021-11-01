
from rest_framework import serializers
from .models import OperateLog
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import OperateLogSerializer
from hlsh_report.utils.baseViewSet import BaseViewSet
import datetime 
from rest_framework.permissions import *
import pendulum
# Create your views here.

class OperateLogViewSet(BaseViewSet):

    permission_classes = [IsAuthenticated]

    queryset = OperateLog.objects.all()
    serializer_class = OperateLogSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['user','operate_time']
    filterset_fields = ['operate_time']
    ordering_fields = ['-operate_time']

    # 只允许GET请求
    http_method_names = ['get']

    def get_queryset(self):
        query_params = self.request.query_params
        print(query_params)
        s = query_params.get('start_time', None)
        e =  query_params.get('end_time', None)
        user = query_params.get('user', None)
        print(s,e)
        print(user)
        start_time = datetime.datetime(year=int(s[0:4]), month=int(s[4:6]), day=int(s[6:8]))
        end_time = datetime.datetime(year=int(e[0:4]), month=int(e[4:6]), day=int(e[6:8]))+datetime.timedelta(days=1)
        # end_time = pendulum.parse(e).subtract(days=1)
        print(start_time,end_time)
        if user is not None:
            return OperateLog.objects.filter(operate_time__range=(start_time, end_time), user=user)
        else:
        
            return OperateLog.objects.filter(operate_time__range=(start_time, end_time))

    
