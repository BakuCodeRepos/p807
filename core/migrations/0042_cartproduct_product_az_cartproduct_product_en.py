# Generated by Django 4.2.7 on 2023-12-11 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_cartproduct_color_az_cartproduct_color_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='product_az',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.clothes'),
        ),
        migrations.AddField(
            model_name='cartproduct',
            name='product_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.clothes'),
        ),
    ]
