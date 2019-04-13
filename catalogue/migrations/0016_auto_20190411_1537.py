# Generated by Django 2.0.7 on 2019-04-11 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0015_auto_20190411_1524'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attribute',
            options={'ordering': ['title'], 'verbose_name_plural': 'Attribute'},
        ),
        migrations.AlterModelOptions(
            name='attributeclass',
            options={'verbose_name_plural': 'Attribute Class Title'},
        ),
        migrations.AlterModelOptions(
            name='attributeproductclass',
            options={'verbose_name_plural': 'Product Attribute Class'},
        ),
        migrations.AlterModelOptions(
            name='attributetitle',
            options={'ordering': ['-ordering_by', 'title'], 'verbose_name_plural': 'Attribute Title'},
        ),
        migrations.RemoveField(
            model_name='attribute',
            name='product_related',
        ),
    ]