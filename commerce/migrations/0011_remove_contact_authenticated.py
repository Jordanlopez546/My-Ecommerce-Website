# Generated by Django 4.1.7 on 2023-04-23 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0010_contact_authenticated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='authenticated',
        ),
    ]
