# Generated by Django 4.2.16 on 2024-12-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0003_alter_item_options_item_base_education_item_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='is_available',
            field=models.BooleanField(default=False, verbose_name='Доступно'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='itemtag',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
    ]
