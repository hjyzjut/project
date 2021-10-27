'''
自己定义一个ViewSet继承DRF的ModalViewSet
'''
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .response import BaseResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from hlsh_report.apps.logs.models import OperateLog
from hlsh_report.apps.logs.serializers import OperateLogSerializer
import datetime
from hlsh_report.utils.reportJson import json_load

class ReportViewSet(ModelViewSet):
    queryset = None
    serializer_class = None
    permission_classes = []
    search_fields = []
    filterset_fields = []
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]


    def create(self, request, *args, **kwargs):
        json_data = request.data
        data = json_load(request)
        # print(type(json_data['user']))
        if isinstance(data, list):
            
            serializer = self.get_serializer(data=data, many=True)
        else:
            serializer = self.get_serializer(data=data)
        # is_valid()方法还可以在验证失败时抛出异常serializers.ValidationError，可以通过传递raise_exception=True参数开启，REST framework接收到此异常，会向前端返回HTTP 400 Bad Request响应
        serializer.is_valid(raise_exception=True)
        print("isinstance:serializer")
        operate_log = OperateLog.objects.create(user=json_data['user'], operate_type='创建',data_model=json_data['template'],file_name=json_data['file_name'],operate_time=datetime.datetime.now())
        self.perform_create(serializer)
        header = self.get_success_headers(serializer.data) 
        return BaseResponse(data=serializer.data, code=201, success=True, msg="创建成功", status=status.HTTP_201_CREATED,headers=header)



    """
    List a queryset.
    """

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            # return self.get_paginated_response(serializer.data)
            return BaseResponse(data=self.get_paginated_response(serializer.data), code=200, msg="success",
                                  success=True, status=status.HTTP_200_OK)

        serializer = self.get_serializer(queryset, many=True)
        return BaseResponse(data=serializer.data, code=200, msg="success", success=True, status=status.HTTP_200_OK)

    """
    Retrieve a model instance.
    """

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return BaseResponse(data=serializer.data, code=200, msg="success", success=True, status=status.HTTP_200_OK)

    """
    Update a model instance.
    """

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return BaseResponse(data=serializer.data, code=200, msg="更新成功", success=True, status=status.HTTP_200_OK)

    # 重构destroy方法

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return BaseResponse(data=[], code=204, msg="删除成功", success=True, status=status.HTTP_204_NO_CONTENT)

