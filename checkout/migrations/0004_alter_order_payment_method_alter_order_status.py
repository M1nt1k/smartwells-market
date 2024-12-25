# Generated by Django 4.2.16 on 2024-12-25 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_shippingaddress_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('invoice', 'Счёт для юридического лица'), ('card_online', 'Картой онлайн')], max_length=20, verbose_name='Способ оплаты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('processing', 'Обрабатывается'), ('completed', 'Выполнен'), ('cancelled', 'Отменен')], default='processing', max_length=20, verbose_name='Статус'),
        ),
    ]