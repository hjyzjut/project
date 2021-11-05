from datetime import date
from hlsh_report.utils.reportViewSet import ReportViewSet
from django.db import models
from django.db.models.base import Model

# Create your models here.
class GmvBudget(models.Model):

    # GMV预算的模型

    # bussiness_type_choices = (
    #     ('授权','0'),
    #     ('自营','1'),
    # )
    id = models.AutoField(primary_key=True)
    bussiness = models.CharField(max_length=30, verbose_name='事业部')
    bussiness_type = models.CharField(max_length=30,  verbose_name='业务类型')
    business_entity = models.CharField(max_length=20, default='海澜优选', verbose_name='经营主体') # 固定默认值
    brand = models.CharField(max_length=30, verbose_name='品牌')
    category = models.CharField(max_length=30 ,verbose_name='类目')
    channel = models.CharField(max_length=30, default='全渠道', verbose_name='渠道') # 固定默认值
    year = models.CharField(max_length=10, verbose_name='年')
    budget_sum = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='当年累计')
    budget_jan = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='1月预算')
    budget_feb = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='2月预算')
    budget_mar = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='3月预算')
    budget_apr = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='4月预算')
    budget_may = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='5月预算')
    budget_jun = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='6月预算')
    budget_jul = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='7月预算')
    budget_aug = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='8月预算')
    budget_sep = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='9月预算')
    budget_oct = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='10月预算')
    budget_nov = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='11月预算')
    budget_dec = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='12月预算')
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
    # bussiness_type_choices = (
    #     ('授权','0'),
    #     ('自营','1'),
    # )

    id = models.AutoField(primary_key=True)

    bussiness = models.CharField(max_length=30, verbose_name='事业部')
    bussiness_type = models.CharField(max_length=30,  verbose_name='业务类型')
    business_entity = models.CharField(max_length=20, default='海澜优选', verbose_name='经营主体') # 固定默认值
    brand = models.CharField(max_length=30, verbose_name='品牌')
    category = models.CharField(max_length=30 ,verbose_name='类目')
    channel = models.CharField(max_length=30, default='全渠道', verbose_name='渠道') # 固定默认值
    year = models.CharField(max_length=10, verbose_name='年度')
    month = models.CharField(max_length=10, verbose_name='月份')

    gmv = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='GMV')
    gsv = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='GSV')

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

    # bussiness_type_choices = (
    #     ('授权','0'),
    #     ('自营','1'),
    # )

    id = models.AutoField(primary_key=True)

    bussiness = models.CharField(max_length=30, verbose_name='事业部')
    bussiness_type = models.CharField(max_length=30,  verbose_name='业务类型')
    business_entity = models.CharField(max_length=20, default='海澜优选', verbose_name='经营主体') # 固定默认值
    brand = models.CharField(max_length=30, verbose_name='品牌')
    category = models.CharField(max_length=30 ,verbose_name='类目')
    channel = models.CharField(max_length=30, default='全渠道', verbose_name='渠道') # 固定默认值
    input_date = models.DateField(verbose_name='入参日期')
    year = models.CharField(max_length=10, verbose_name='年度')
    week = models.CharField(max_length=10, verbose_name='周数')

    gmv = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='GMV')

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
    channel = models.CharField(max_length=30,  verbose_name='渠道') # 固定默认值
    year = models.CharField(max_length=10, verbose_name='年')
    guaranteed_sum = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='当年累计')
    guaranteed_jan = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='1月保底')
    guaranteed_feb = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='2月保底')
    guaranteed_mar = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='3月保底')
    guaranteed_apr = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='4月保底')
    guaranteed_may = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='5月保底')
    guaranteed_jun = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='6月保底')
    guaranteed_jul = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='7月保底')
    guaranteed_aug = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='8月保底')
    guaranteed_sep = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='9月保底')
    guaranteed_oct = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='10月保底')
    guaranteed_nov = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='11月保底')
    guaranteed_dec = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='12月保底')

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
        super(GuaranteedLicenseIncome, self).save(*args,**kwargs)
    
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

    license_income = models.DecimalField(max_digits=16, decimal_places=8,  verbose_name='授权收入')

    user = models.CharField(max_length=30, verbose_name='用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # auto_now_add创建时自动将创建的时间插入
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')  # auto_now更新时自动将时间插入

    class Meta:
        db_table = 'real_license_income_info'
        verbose_name = '授权收入-实际'
        verbose_name_plural = verbose_name
        ordering = ['-id','-create_time']


class AuthorizedShop(models.Model):
  
    id = models.AutoField(primary_key=True)

    bussiness = models.CharField(max_length=30, verbose_name='事业部', null=True, blank=True)
    brand = models.CharField(max_length=30, verbose_name='品牌', null=True, blank=True)
    category = models.CharField(max_length=30, verbose_name='类目', null=True, blank=True)
    channel = models.CharField(max_length=50, verbose_name='渠道', null=True, blank=True)
    authorized_dealer = models.CharField(max_length=500, verbose_name='客户')
    certificate_number = models.CharField(max_length=100, verbose_name='证书编号（红色为盖章中）', null=True, blank=True)
    first_party = models.CharField(max_length=500, verbose_name='授权方/甲方', null=True, blank=True)
    second_party = models.CharField(max_length=500, verbose_name='被授权方/乙方', null=True, blank=True)
    nature_of_the_licensee = models.CharField(max_length=100, verbose_name='被授权方性质', null=True, blank=True)
    authorized_brand = models.CharField(max_length=500, verbose_name='授权品牌', null=True, blank=True)
    trademark_category = models.CharField(max_length=50, verbose_name='商标类别', null=True, blank=True)
    authorization_category = models.CharField(max_length=500, verbose_name='授权品类', null=True, blank=True)
    shop_name_planning = models.CharField(max_length=500, verbose_name='申请店铺名称（销售授权）；地址（产品生产授权）', null=True, blank=True)
    actual_shop_name = models.CharField(max_length=500, verbose_name='最终店铺名称【业务报备白名单店铺】', null=True, blank=True)
    authorized_platform = models.CharField(max_length=100, verbose_name='授权平台', null=True, blank=True)
    licensing_mode = models.CharField(max_length=100, verbose_name='授权许可方式', null=True, blank=True)
    authorization_start_time = models.DateField(verbose_name='授权起始日', null=True, blank=True)
    authorization_end_time = models.DateField(verbose_name='授权终止日', null=True, blank=True)
    issue_time = models.DateField(verbose_name='签发日期', null=True, blank=True)
    remark = models.CharField(max_length=500, verbose_name='备注', null=True, blank=True)
    platform_verified_authorization = models.CharField(max_length=500, verbose_name='平台核实授权书', null=True, blank=True)
    certificate_status = models.CharField(max_length=100, verbose_name='证书状态', null=True, blank=True)
    shop_status = models.CharField(max_length=100, verbose_name='店铺状态', null=True, blank=True)


    user = models.CharField(max_length=30, verbose_name='用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # auto_now_add创建时自动将创建的时间插入
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')  # auto_now更新时自动将时间插入
    
    class Meta:
        db_table = 'authorized_shop'
        verbose_name = '授权开店清单'
        verbose_name_plural = verbose_name
        ordering = ['-id', '-create_time']



class DoubleEleven(models.Model):
  
    id = models.AutoField(primary_key=True)

    data_time = models.DateField(verbose_name='日期',null=True, blank=True)
    data_hours = models.CharField(max_length=10, verbose_name='小时',null=True, blank=True)
    plat = models.CharField(max_length=20, verbose_name='平台', null=True, blank=True)
    shop_name = models.CharField(max_length=50, verbose_name='店铺名称', null=True, blank=True)
    brand = models.CharField(max_length=30, verbose_name='品牌', null=True, blank=True)
    sales = models.DecimalField(max_digits=32, decimal_places=8,  verbose_name='商品销量', null=True, blank=True)
    order_num = models.IntegerField(verbose_name='订单数量', null=True, blank=True)
    unique_visitor = models.IntegerField(verbose_name='访客数', null=True, blank=True)
    avg_transaction_val = models.DecimalField(max_digits=32, decimal_places=8,  verbose_name='客单价', null=True, blank=True)
    transaction_amount = models.DecimalField(max_digits=32, decimal_places=8,  verbose_name='成交金额', null=True, blank=True)

    
    user = models.CharField(max_length=30, verbose_name='用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # auto_now_add创建时自动将创建的时间插入
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')  # auto_now更新时自动将时间插入

    class Meta:
        db_table = 'double_eleven'
        verbose_name = '双十一大屏'
        verbose_name_plural = verbose_name
        ordering = ['-id', '-create_time']
