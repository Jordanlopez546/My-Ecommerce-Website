# Generated by Django 4.1.6 on 2023-04-21 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0005_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='shipping_fee',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]