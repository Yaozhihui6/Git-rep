# Generated by Django 2.1.8 on 2019-06-02 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Webcar', '0025_auto_20190602_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='orderstarttime',
            new_name='充电开始时间',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='oedertime',
            new_name='充电时长',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='orderactiontype',
            new_name='充电行为类型编号',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='orderpilenumber',
            new_name='电桩编号',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='orderphone',
            new_name='联系电话',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='ordercredit',
            new_name='订单分值小计',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='ordernumber',
            new_name='订单号',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='ordercarnumber',
            new_name='车牌号',
        ),
        migrations.AlterField(
            model_name='chargeerror',
            name='订单号',
            field=models.ForeignKey(db_column='订单号', on_delete=django.db.models.deletion.DO_NOTHING, to='Webcar.Orders', to_field='ordernumber'),
        ),
    ]
