# Generated by Django 2.2.13 on 2021-11-01 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoubleEleven',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_time', models.DateField(blank=True, null=True, verbose_name='日期')),
                ('data_hours', models.CharField(blank=True, max_length=10, null=True, verbose_name='小时')),
                ('plat', models.CharField(blank=True, max_length=20, null=True, verbose_name='平台')),
                ('shop_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='店铺名称')),
                ('brand', models.CharField(blank=True, max_length=30, null=True, verbose_name='品牌')),
                ('sales', models.DecimalField(blank=True, decimal_places=8, max_digits=16, null=True, verbose_name='商品销量')),
                ('order_num', models.IntegerField(blank=True, null=True, verbose_name='订单数量')),
                ('transaction_amount', models.DecimalField(blank=True, decimal_places=8, max_digits=16, null=True, verbose_name='成交金额')),
                ('user', models.CharField(max_length=30, verbose_name='用户')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '双十一大屏',
                'verbose_name_plural': '双十一大屏',
                'db_table': 'double_eleven',
                'ordering': ['-id', '-create_time'],
            },
        ),
    ]