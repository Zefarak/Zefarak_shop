# Generated by Django 2.0.7 on 2019-04-14 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0016_auto_20190412_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_expired',
            field=models.DateField(default=datetime.datetime(2019, 4, 14, 8, 39, 52, 217048), verbose_name='Date'),
        ),
    ]