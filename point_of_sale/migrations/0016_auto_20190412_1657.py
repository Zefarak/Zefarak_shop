# Generated by Django 2.0.7 on 2019-04-12 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0015_auto_20190411_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_expired',
            field=models.DateField(default=datetime.datetime(2019, 4, 12, 16, 57, 28, 577170), verbose_name='Date'),
        ),
    ]
