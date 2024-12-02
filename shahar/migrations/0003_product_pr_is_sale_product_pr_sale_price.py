# Generated by Django 4.2.13 on 2024-07-31 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shahar', '0002_product_pr_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pr_is_sale',
            field=models.BooleanField(default=False, verbose_name='فروش ویژه'),
        ),
        migrations.AddField(
            model_name='product',
            name='pr_sale_price',
            field=models.IntegerField(default=0, verbose_name='قیمت تخفیف'),
        ),
    ]
