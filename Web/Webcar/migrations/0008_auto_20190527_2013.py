# Generated by Django 2.1.8 on 2019-05-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webcar', '0007_auto_20190527_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='账号',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
