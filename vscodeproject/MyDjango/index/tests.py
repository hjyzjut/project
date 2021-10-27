from django.test import TestCase
# from MyDjango.index.models import *

# Create your tests here.
#
#     # 数据表的读写
#     # 1
#     P1 = Product()
#     P1.name = '荣耀V9'
#     P1.weight = '119g'
#     P1.size = '120*75*7mm'
#     P1.type_id = 2
#     P1.save()
#     # 2
#     P2 = Product.objects.create(name='HUAWEI 20', weight='120g', size='120*75*7mm', type=3)
#     # 3
#     P2 = Product(name='HUAWEI P30', weight='64g', size='120*75*7mm', type_id=2)
#     P2.save()

# select
# 单条
# Product.objects.get(id=1)
# 多条
# Product.objects.filter(name='HUAWEI 20')

# update
# Product.objects.get(id=1).update(name='111')
# Product.objects.filter(name='HUAWEI 20').update(name='2222')
# Product.objects.update(name='333')

# drop
# Product.objects.all().delete()
# Product.objects.get(id=1).delete()
# Product.objects.filter(name='HUAWEI 20').delete()