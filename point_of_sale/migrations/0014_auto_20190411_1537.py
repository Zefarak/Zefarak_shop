# Generated by Django 2.0.7 on 2019-04-11 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0013_auto_20190411_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_expired',
            field=models.DateField(default=datetime.datetime(2019, 4, 11, 15, 37, 56, 917631), verbose_name='Date'),
        ),
    ]
