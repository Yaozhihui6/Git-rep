from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    联系电话 = models.CharField(primary_key=True, max_length=11)
    用户类型 = models.IntegerField(blank=True, null=True, default=0)
    集团编号 = models.IntegerField(blank=True, null=True)
    集团名 = models.CharField(max_length=50, blank=True, null=True)
    用户密码 = models.CharField(max_length=255, blank=True, null=True)
    用户姓名 = models.CharField(max_length=20, blank=True, null=True)
    账号 = models.CharField(max_length=50, blank=True, null=True)
    邮箱 = models.CharField(max_length=50, blank=True, null=True)
    车牌号 = models.CharField(max_length=10, blank=True, null=True)
    信用分值 = models.IntegerField(blank=True, null=True, default=500)

    class Meta:
        managed = True
        db_table = '用户'

class Admins(models.Model):
    管理员联系电话 = models.CharField(primary_key=True, max_length=11)
    管理员密码 = models.CharField(max_length=255, blank=True, null=True)
    管理员姓名 = models.CharField(max_length=20, blank=True, null=True)
    管理员工号 = models.IntegerField(blank=True, null=True)
    管理员邮箱 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = '管理员'


class ErrorType(models.Model):
    充电行为类型编号 = models.IntegerField(primary_key=True)
    充电行为类型 = models.CharField(max_length=40, blank=True, null=True)
    行为分值 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = '充电故障'


class Orders(models.Model):
    订单号 = models.CharField(primary_key=True, max_length=30)
    联系电话 = models.ForeignKey(Users,on_delete = models.DO_NOTHING, db_column='联系电话', blank=True, null=True)
    车牌号 = models.CharField(max_length=10, blank=True, null=True)
    充电开始时间 = models.CharField(max_length=255, blank=True, null=True)
    充电时长 = models.IntegerField(blank=True, null=True)
    电桩编号 = models.CharField(max_length=6, blank=True, null=True)
    充电行为类型编号 = models.IntegerField(blank=True, null=True)
    订单分值小计 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = '订单'


class ChargeError(models.Model):
    订单号 = models.ForeignKey(Orders,on_delete = models.DO_NOTHING, db_column='订单号')
    联系电话 = models.ForeignKey(Users,on_delete = models.DO_NOTHING, db_column='联系电话')
    充电行为类型编号 = models.IntegerField(blank=True, null=True)
    车牌号 = models.CharField(max_length=10, blank=True, null=True)
    信用分值小计 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = '充电行为'


class Subs(models.Model):
    预约号 = models.CharField(primary_key=True, max_length=30)
    联系电话 = models.ForeignKey(Users,on_delete = models.DO_NOTHING, db_column='联系电话')
    电桩编号 = models.CharField(max_length=6, blank=True, null=True)
    车牌号 = models.CharField(max_length=10, blank=True, null=True)
    预约充电开始时间 = models.CharField(max_length=255, blank=True, null=True)
    预约充电时长 = models.IntegerField(blank=True, null=True)
    预约状态 = models.IntegerField(blank=True, null=True)
    预约分值小计 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = '预约'

