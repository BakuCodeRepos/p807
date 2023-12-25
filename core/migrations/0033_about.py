# Generated by Django 4.2.7 on 2023-12-07 11:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_cartproduct_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('our_story_text', ckeditor.fields.RichTextField()),
                ('our_story_image', models.ImageField(blank=True, null=True, upload_to='media/product_images/')),
                ('our_mission_text', ckeditor.fields.RichTextField()),
                ('our_mission_image', models.ImageField(blank=True, null=True, upload_to='media/product_images/')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
        ),
    ]