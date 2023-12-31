# Generated by Django 4.2.5 on 2023-11-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_cartproduct_options_alter_categories_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlogCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'BlogCategories',
                'verbose_name_plural': 'BlogCategories',
            },
        ),
    ]
