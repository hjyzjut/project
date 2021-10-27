from django.db import models

# Create your models here.

class OperateLog(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=30, verbose_name='账号')
    operate_type = models.CharField(max_length=30,default='数据填报', verbose_name='操作类型')
    data_model = models.CharField(max_length=30, verbose_name='填报模版')
    file_name = models.TextField(max_length=200, default='-', verbose_name='上传文件名')
    operate_time = models.DateTimeField(verbose_name='操作时间')


    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # auto_now_add创建时自动将创建的时间插入


    class Meta:
        db_table = 'operate_log'
        verbose_name = '操作日志'
        verbose_name_plural = verbose_name
        ordering = ['-operate_time']