# Generated by Django 2.1.8 on 2019-05-27 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webcar', '0002_auto_20190526_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='信用分值',
            field=models.IntegerField(blank=True, default=500, null=True),
        ),
    ]
