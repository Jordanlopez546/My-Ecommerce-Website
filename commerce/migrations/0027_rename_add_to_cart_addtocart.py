# Generated by Django 4.1.6 on 2023-06-29 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0026_add_to_cart_delete_cartscount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Add_To_Cart',
            new_name='AddToCart',
        ),
    ]