# Generated by Django 4.2.5 on 2023-11-20 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_clothes_name_az_clothes_name_en'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothes',
            name='name_az',
        ),
        migrations.RemoveField(
            model_name='clothes',
            name='name_en',
        ),
    ]
