# Generated by Django 4.2.5 on 2023-11-15 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_cartproduct'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartproduct',
            options={'verbose_name_plural': 'Cart products'},
        ),
        migrations.AddField(
            model_name='cartproduct',
            name='overall_sum',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
