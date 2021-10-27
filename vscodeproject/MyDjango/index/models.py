from django.db import models
from django.utils.html import format_html


# Create your models here.
class Type(models.Model):
    id = models.AutoField(verbose_name='序号', primary_key=True)
    type_name = models.CharField(verbose_name='产品类型', max_length=20)

    # 设置返回值，如不设置，默认返回Type对象
    def __str__(self):
        return self.type_name


class Product(models.Model):
    id = models.AutoField(verbose_name='序号', primary_key=True)
    name = models.CharField(verbose_name='名称', max_length=50)
    weight = models.CharField(verbose_name='重量', max_length=20)
    size = models.CharField(verbose_name='尺寸', max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='产品类型')

    # 设置返回值
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '产品信息'
        verbose_name_plural = '产品信息'

    # 自定义函数，设置字体颜色
    def colored_type(self):
        if '手机' in self.type.type_name:
            color_code = 'red'
        elif '平板电脑' in self.type.type_name:
            color_code = 'blue'
        elif '智能穿戴' in self.type.type_name:
            color_code = 'green'
        else:
            color_code = 'yellow'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.type
        )
    # 设置Admin的标题
    colored_type.short_description = '带颜色的产品类型'
# 一对一
# class Performer(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=20)
#     nationality = models.CharField(max_length=20)
#     masterpiece = models.CharField(max_length=20)
#
#
# class Performer_info(models.Model):
#     id = models.IntegerField(primary_key=True)
#     performer = models.OneToOneField(Performer, on_delete=models.CASCADE)
#     birth = models.CharField(max_length=20)
#     elapse = models.CharField(max_length=20)

# 一对多
# class Performer(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=20)
#     nationality = models.CharField(max_length=20)
#
#
# class Program(models.Model):
#     id = models.IntegerField(primary_key=True)
#     performer = models.ForeignKey(Performer, on_delete=models.CASCADE)
#     name = models.CharField(max_length=20)

# 多对多
# class Performer(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=20)
#     nationality = models.CharField(max_length=20)
#
#
# class Program(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=20)
#     performer = models.ManyToManyField(Performer)

# python manage.py makemigrations：
#     用于将index所定义的模型生成001_initial.py文件，该文件存放在index的migrations文件夹
# python manage.py migrate：
#     根据脚本在目标数据库中生成对应的数据表
