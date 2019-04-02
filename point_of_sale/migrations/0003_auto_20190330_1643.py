# Generated by Django 2.0.7 on 2019-03-30 14:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0012_auto_20190329_1922'),
        ('point_of_sale', '0002_auto_20190329_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItemAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('attr_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.AttributeClass')),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='point_of_sale.OrderItem')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.Attribute')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='date_expired',
            field=models.DateField(default=datetime.datetime(2019, 3, 30, 16, 43, 16, 516014), verbose_name='Date'),
        ),
    ]