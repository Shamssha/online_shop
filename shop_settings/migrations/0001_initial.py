# Generated by Django 4.2.13 on 2024-11-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='موبایل')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل آدرس')),
            ],
        ),
    ]
