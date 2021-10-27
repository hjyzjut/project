from hlsh_report.utils.reportViewSet import ReportViewSet
from django.db import models
from django.db.models.base import Model

# Create your models here.
class GmvBudget(models.Model):

    # GMV预算的模型

    bussiness_type_choices = (
        ('授权','0'),
        ('自营','1'),
    )
    id = models.AutoField(primary_key=True)
    bussiness = models.CharField(max_length=30, verbose_name='事业部')
    bussiness_type = models.CharField(max_length=30, choices=bussiness_type_choices, verbose_name='业务类型')
    business_entity = models.CharField(max_length=20, default='海澜优选', verbose_name='经营主体') # 固定默认值
    brand = models.CharField(max_length=30, verbose_name='品牌')
    category = models.CharField(max_length=30 ,verbose_name='类目')
    channel = models.CharField(max_length=30, default='全渠道', verbose_name='渠道') # 固定默认值
    year = models.CharField(max_length=10, verbose_name='年')
    budget_sum = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='当年累计')
    budget_jan = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='1月预算')
    budget_feb = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='2月预算')
    budget_mar = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='3月预算')
    budget_apr = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='4月预算')
    budget_may = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='5月预算')
    budget_jun = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='6月预算')
    budget_jul = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='7月预算')
    budget_aug = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='8月预算')
    budget_sep = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='9月预算')
    budget_oct = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='10月预算')
    budget_nov = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='11月预算')
    budget_dec = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='12月预算')
    user = models.CharField(max_length=30, verbose_name='用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # auto_now_add创建时自动将创建的时间插入
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')  # auto_now更新时自动将时间插入

    @property
    def get_budget_sum(self):
        first_half_year = self.budget_jan+self.budget_feb+self.budget_mar+self.budget_apr+self.budget_may+self.budget_jun
        second_half_year = self.budget_jul+self.budget_aug+self.budget_sep+self.budget_oct+self.budget_nov+self.budget_dec
        return first_half_year+second_half_year
    

    def save(self, *args, **kwargs):
        self.budget_sum = self.get_budget_sum
        super(GmvBudget, self).save(*args,**kwargs)
    
    class Meta:
        db_table = 'gmv_budget_info'
        verbose_name = 'GMV预算'
        verbose_name_plural = verbose_name
        ordering = ['-id','-create_time']


class GmvGsvReal(models.Model):

    # GMV&GSV实际
    bussiness_type_choices = (
        ('授权','0'),
        ('自营','1'),
    )

    id = models.AutoField(primary_key=True)

    bussiness = models.CharField(max_length=30, verbose_name='事业部')
    bussiness_type = models.CharField(max_length=30, choices=bussiness_type_choices, verbose_name='业务类型')
    business_entity = models.CharField(max_length=20, default='海澜优选', verbose_name='经营主体') # 固定默认值
    brand = models.CharField(max_length=30, verbose_name='品牌')
    category = models.CharField(max_length=30 ,verbose_name='类目')
    channel = models.CharField(max_length=30, default='全渠道', verbose_name='渠道') # 固定默认值
    year = models.CharField(max_length=10, verbose_name='年度')
    month = models.CharField(max_length=10, verbose_name='月份')

    gmv = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='GMV')
    gsv = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='GSV')

    user = models.CharField(max_length=30, verbose_name='用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # auto_now_add创建时自动将创建的时间插入
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')  # auto_now更新时自动将时间插入

    class Meta:
        db_table = 'gmv_gsv_real_info'
        verbose_name = 'GMV&GSV实际'
        verbose_name_plural = verbose_name
        ordering = ['-id','-create_time']


class GmvWeekReal(models.Model):

    # GMV周实际

    bussiness_type_choices = (
        ('授权','0'),
        ('自营','1'),
    )

    id = models.AutoField(primary_key=True)

    bussiness = models.CharField(max_length=30, verbose_name='事业部')
    bussiness_type = models.CharField(max_length=30, choices=bussiness_type_choices, verbose_name='业务类型')
    business_entity = models.CharField(max_length=20, default='海澜优选', verbose_name='经营主体') # 固定默认值
    brand = models.CharField(max_length=30, verbose_name='品牌')
    category = models.CharField(max_length=30 ,verbose_name='类目')
    channel = models.CharField(max_length=30, default='全渠道', verbose_name='渠道') # 固定默认值
    input_date = models.DateField(verbose_name='入参日期')
    year = models.CharField(max_length=10, verbose_name='年度')
    week = models.CharField(max_length=10, verbose_name='周数')

    gmv = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='GMV')

    user = models.CharField(max_length=30, verbose_name='用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # auto_now_add创建时自动将创建的时间插入
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')  # auto_now更新时自动将时间插入

    class Meta:
        db_table = 'gmv_week_real_info'
        verbose_name = 'GMV周实际'
        verbose_name_plural = verbose_name
        ordering = ['-id','-create_time']


class GuaranteedLicenseIncome(models.Model):

    # 授权收入-保底

    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=30, verbose_name='品牌')
    category = models.CharField(max_length=30 ,verbose_name='类目')
    channel = models.CharField(max_length=30, default='全渠道', verbose_name='渠道') # 固定默认值
    year = models.CharField(max_length=10, verbose_name='年')
    guaranteed_sum = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='当年累计')
    guaranteed_jan = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='1月保底')
    guaranteed_feb = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='2月保底')
    guaranteed_mar = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='3月保底')
    guaranteed_apr = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='4月保底')
    guaranteed_may = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='5月保底')
    guaranteed_jun = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='6月保底')
    guaranteed_jul = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='7月保底')
    guaranteed_aug = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='8月保底')
    guaranteed_sep = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='9月保底')
    guaranteed_oct = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='10月保底')
    guaranteed_nov = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='11月保底')
    guaranteed_dec = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='12月保底')

    user = models.CharField(max_length=30, verbose_name='用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # auto_now_add创建时自动将创建的时间插入
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')  # auto_now更新时自动将时间插入


    @property
    def get_guaranteed_sum(self):
        first_half_year = self.guaranteed_jan+self.guaranteed_feb+self.guaranteed_mar+self.guaranteed_apr+self.guaranteed_may+self.guaranteed_jun
        second_half_year = self.guaranteed_jul+self.guaranteed_aug+self.guaranteed_sep+self.guaranteed_oct+self.guaranteed_nov+self.guaranteed_dec
        return first_half_year+second_half_year
    

    def save(self, *args, **kwargs):
        self.guaranteed_sum = self.get_guaranteed_sum
        super(GmvBudget, self).save(*args,**kwargs)
    
    class Meta:
        db_table = 'guaranteed_license_income_info'
        verbose_name = '授权收入-保底'
        verbose_name_plural = verbose_name
        ordering = ['-id','-create_time']


class RealLicenseIncome(models.Model):
    
    # 授权收入-实际

    id = models.AutoField(primary_key=True)

    bussiness = models.CharField(max_length=30, verbose_name='事业部')
    brand = models.CharField(max_length=30, verbose_name='品牌')
    category = models.CharField(max_length=30 ,verbose_name='类目')
    channel = models.CharField(max_length=30, default='全渠道', verbose_name='渠道') # 固定默认值
    year = models.CharField(max_length=10, verbose_name='年度')
    month = models.CharField(max_length=10, verbose_name='月份')

    license_income = models.DecimalField(max_digits=16, decimal_places=2, default=0.00, verbose_name='授权收入')

    user = models.CharField(max_length=30, verbose_name='用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # auto_now_add创建时自动将创建的时间插入
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')  # auto_now更新时自动将时间插入

    class Meta:
        db_table = 'real_license_income_info'
        verbose_name = '授权收入-实际'
        verbose_name_plural = verbose_name
        ordering = ['-id','-create_time']