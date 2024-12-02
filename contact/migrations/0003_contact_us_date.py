# Generated by Django 4.2.13 on 2024-10-02 10:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_us_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ'),
            preserve_default=False,
        ),
    ]
