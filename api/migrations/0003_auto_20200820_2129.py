# Generated by Django 3.1 on 2020-08-20 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200820_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(default=0, max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
