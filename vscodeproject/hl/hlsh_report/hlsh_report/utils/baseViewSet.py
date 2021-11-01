'''
自己定义一个ViewSet继承DRF的ModalViewSet
'''
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .response import BaseResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.views import TokenViewBase

class BaseViewSet(ModelViewSet):
    queryset = None
    serializer_class = None
    permission_classes = []
    search_fields = []
    filterset_fields = []
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]


    def create(self, request, *args, **kwargs):
        json_data = request.data
        print(json_data['data'])
        if isinstance(json_data['data'], list):
            serializer = self.get_serializer(data=json_data['data'], many=True)
        else:
            serializer = self.get_serializer(data=json_data['data'])
        # is_valid()方法还可以在验证失败时抛出异常serializers.ValidationError，可以通过传递raise_exception=True参数开启，REST framework接收到此异常，会向前端返回HTTP 400 Bad Request响应
        serializer.is_valid(raise_exception=True)
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
        # 当有is_deleted字段时修改为false，无时删除数据库条目
        if (instance.is_delete != None):
            instance.is_delete = True
            self.perform_update(instance)
        else:
            self.perform_destroy(instance)
        return BaseResponse(data=[], code=204, msg="删除成功", success=True, status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = serializers.TokenObtainPairSerializer

    # 重写post方法
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return BaseResponse(data=serializer.validated_data, status=status.HTTP_200_OK, code=200, msg="success",
                              success=True, )
