# Generated by Django 2.1.8 on 2019-06-02 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Webcar', '0020_auto_20190602_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chargeerror',
            old_name='电话',
            new_name='联系电话',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='订单电话',
            new_name='联系电话',
        ),
        migrations.RenameField(
            model_name='subs',
            old_name='预约电话',
            new_name='联系电话',
        ),
    ]
