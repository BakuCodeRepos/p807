# Generated by Django 4.2.5 on 2023-11-20 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_blog_image_alter_clothes_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothes',
            name='description_az',
        ),
        migrations.RemoveField(
            model_name='clothes',
            name='description_en',
        ),
    ]
