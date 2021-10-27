from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from .models import Product
from django.views.generic import ListView
from .form import *


# Create your views here.


# def index(request):
#     return render(request, 'index.html', context={'title': '首页'}, status=500)
# def index(request):
#     type_list = Product.objects.values('type').distinct()
#     name_list = Product.objects.values('name', 'type')
#     context = {'title': '首页', 'type_list': type_list, 'name_list': name_list}
#     return render(request, 'index.html', context=context, status=200)

def index(request):
    if request.method == 'GET':

        product = ProductForm()
        return render(request, 'data_form.html', locals())
    else:
        product = ProductForm(request.POST)
        if product.is_valid():
            # 方法一
            name = product['name']
            # 方法二：cleaned_data将控件name的数据进行清洗，转换成python数据类型
            cname = product.cleaned_data['name']
            return HttpResponse('提交成功')
        else:
            # 将错误信息输出，error_msg是将错误信息以json格式输出
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'data_form.html', locals())


def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        # 绝对路径，完整的地址信息
        # return redirect('http://127.0.0.1:8000/')
        # 相对路径，代表首页地址
        return redirect('/')
    else:
        if request.GET.get('name'):
            name = request.GET.get('name')
        else:
            name = 'Everyone'
        return HttpResponse('usename is ' + name)


def model_index(request, id):
    if request.method == 'GET':
        instance = Product.objects.filter(id=id)
        # 判断数据是否存在
        if instance:
            product = ProductModelForm(instance=instance[0])
        else:
            product = ProductModelForm()
        return render(request, 'data_form.html', locals())
    else:
        product = ProductModelForm(request.POST)
        if product.is_valid():
            # 获取weight的数据，并通过clean_weight进行清洗，转换成Python数据类型
            weight = product.cleaned_data['weight']
            # 直接保存到数据库
            # product.save()
            # save方法设置commit=False，生成数据库对象product_db，然后可对该对象的属性值修改并保存
            product_db = product.save(commit=False)
            product_db.name = '我的iPhone'
            product_db.save()
            # save_m2m()方法是保存ManyToMany的数据模型
            # product.save_m2m()
            return HttpResponse('提交成功!weight清洗后的数据为：' + weight)
        else:
            # 将错误信息输出，error_msg是将错误信息以json格式输出
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'data_form.html', locals())


class ProductList(ListView):
    # HTML模版的变量名称
    context_object_name = 'type_list'
    # 设定HTML模版
    template_name = 'index_view.html'
    # 查询数据
    queryset = Product.objects.values('type').distinct()

    # 添加其他变量
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_list'] = Product.objects.values('name', 'type')
        return context

    def get_queryset(self):
        # 获取URL的变量id
        print(self.kwargs['id'])
        # 获取URL的参数name
        print(self.kwargs['name'])
        # 获取请求方式
        print(self.request.method)
        type_list = Product.objects.values('type').distinct()
        return type_list


# 带变量的URL的视图函数
def mydate(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))


# 参数name的URL的视图函数
def myyear(request, year):
    return render(request, 'myyear.html')


# 参数为字典的URL的视图函数
def myyear_dict(request, year, month):
    return render(request, 'myyear_dict.html', {'month': month})


def download(request):
    # 当接收到用户的请求后，视图函数download首先定义HttpResponse的相应类型为文件（text/csv）类型，生成response对象
    response = HttpResponse(content_type='text/csv')
    # 然后在response对象上定义Content-Disposition，设置浏览器下载文件名称。attachment设置文件的下载方式，filename为文件名
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    # 最后使用csv模块加载response对象，把数据写入response对象所设置的csv文件并将response对象返回到浏览器上，从而实现文件下载
    writer = csv.writer(response)
    writer.writerow(['First row', 'A', 'B', 'C'])
    return response
# render(request,template_name,context=None,content_type=None,status=None,using=None)
#       request：浏览器向服务器发送的请求对象，包含用户信息，请求内容和请求方式等。
#       template_name：HTML模版文件名，用于生成HTML网页。
#       context：对HTML模版的变量赋值，以字典格式表示，默认情况下是一个空字典。
#       content_type：响应数据的数据格式，一般情况下使用默认值即可。
#       status：HTTP响应码，默认为200。
#       using：设置HTML模版转换生成HTML网页的模版引擎。
