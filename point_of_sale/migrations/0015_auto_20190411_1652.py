# Generated by Django 2.0.7 on 2019-04-11 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0014_auto_20190411_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_expired',
            field=models.DateField(default=datetime.datetime(2019, 4, 11, 16, 52, 2, 633200), verbose_name='Date'),
        ),
    ]
