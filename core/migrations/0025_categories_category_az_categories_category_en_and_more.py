# Generated by Django 4.2.5 on 2023-11-30 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_tags_tag_az_tags_tag_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='category_az',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='categories',
            name='category_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sizes',
            name='size_az',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sizes',
            name='size_en',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
