from re import I
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import *
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from hlsh_report.utils.baseViewSet import BaseViewSet
from hlsh_report.utils.response import BaseResponse
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework_simplejwt.authentication import *
# Create your views here.

User = get_user_model()

class UserViewSet(BaseViewSet):
    """
    创建用户
    """
    serializer_class = UserSerializer
    # queryset = User.objects.all()
    # print(queryset)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['id','username']
    filterset_fields = ['id','username']

    permission_classes_by_action = {'create': [AllowAny],
                                    'list': [IsAuthenticated],
                                    'update': [IsAuthenticated],
                                    'retrieve': [AllowAny],
                                    'destroy': [AllowAny]
                                    }

    
    # authentication_classes = ([])

    
    # 根据action获取权限
    def get_permissions(self):
        # print('action{}'.format(self.action))
        try:
            return [permissions() for permissions in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permissions() for permissions in self.permission_classes]


    # 重写 get_authenticators函数
    def get_authenticators(self):
        # print('username{}'.format(self.request.user))
        # print(self.authentication_classes)
        """
        Instantiates and returns the list of authenticators that this view can use.
        """
        if self.request.method in ('POST'):
            self.authentication_classes = ([])
        

        return [auth() for auth in self.authentication_classes]



    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        # 添加自己的逻辑，生成token并返回
        refresh = RefreshToken.for_user(user)
        tokens_for_user = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            # 数据定制化
            'username': user.username,  # 由于前端也需要传入username，需要将其加上。cookie.setCookie('name', response.data.username, 7);
        }

        headers = self.get_success_headers(serializer.data)
        return BaseResponse(data=tokens_for_user, success=True, msg="用户注册成功", status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = User.objects.all()
        username = self.request.query_params.get('username', None)
        # print(username)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset
