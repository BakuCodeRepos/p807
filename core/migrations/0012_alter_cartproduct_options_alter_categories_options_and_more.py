# Generated by Django 4.2.5 on 2023-11-20 07:08

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_cartproduct_overall_sum'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartproduct',
            options={'verbose_name': 'Cart products', 'verbose_name_plural': 'Cart products'},
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Categories', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='clothes',
            options={'verbose_name': 'Clothes', 'verbose_name_plural': 'Clothes'},
        ),
        migrations.AlterModelOptions(
            name='colors',
            options={'verbose_name': 'Colors', 'verbose_name_plural': 'Colors'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contact'},
        ),
        migrations.AlterModelOptions(
            name='logo',
            options={'verbose_name': 'Logo', 'verbose_name_plural': 'Logo'},
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Settings', 'verbose_name_plural': 'Settings'},
        ),
        migrations.AlterModelOptions(
            name='sizes',
            options={'verbose_name': 'Sizes', 'verbose_name_plural': 'Sizes'},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'Tags', 'verbose_name_plural': 'Tags'},
        ),
        migrations.AddField(
            model_name='clothes',
            name='category_az',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.categories'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='category_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.categories'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='color_az',
            field=models.ManyToManyField(null=True, to='core.colors'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='color_en',
            field=models.ManyToManyField(null=True, to='core.colors'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='description_az',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='clothes',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='clothes',
            name='materials_az',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='clothes',
            name='materials_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='clothes',
            name='name_az',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='clothes',
            name='name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='clothes',
            name='tag_az',
            field=models.ManyToManyField(null=True, to='core.tags'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='tag_en',
            field=models.ManyToManyField(null=True, to='core.tags'),
        ),
    ]