# Generated by Django 3.2.13 on 2022-11-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pay',
            field=models.IntegerField(),
        ),
    ]