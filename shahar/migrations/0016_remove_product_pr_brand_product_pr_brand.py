# Generated by Django 4.2.13 on 2024-11-10 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shahar', '0015_alter_product_pr_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pr_brand',
        ),
        migrations.AddField(
            model_name='product',
            name='pr_brand',
            field=models.ManyToManyField(related_name='brands', to='shahar.brand', verbose_name='برند'),
        ),
    ]
