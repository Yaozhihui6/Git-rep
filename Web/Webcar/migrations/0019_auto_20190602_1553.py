# Generated by Django 2.1.8 on 2019-06-02 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Webcar', '0018_remove_users_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chargeerror',
            old_name='联系电话',
            new_name='订单电话',
        ),
        migrations.RenameField(
            model_name='subs',
            old_name='联系电话',
            new_name='预约电话',
        ),
    ]
