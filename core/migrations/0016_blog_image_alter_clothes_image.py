# Generated by Django 4.2.5 on 2023-11-20 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_blog_options_alter_blogcategories_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='media/blog_images/'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/product_images/'),
        ),
    ]
