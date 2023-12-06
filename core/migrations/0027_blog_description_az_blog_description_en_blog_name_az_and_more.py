# Generated by Django 4.2.5 on 2023-11-30 06:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_clothes_description_az_clothes_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description_az',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='name_az',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='name_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='blogcategories',
            name='category_az',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='blogcategories',
            name='category_en',
            field=models.CharField(max_length=50, null=True),
        ),
    ]