# Generated by Django 2.1.3 on 2018-11-21 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(default='', max_length=250),
        ),
    ]