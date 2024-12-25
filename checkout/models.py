from django.contrib.auth.models import User
from django.db import models

# from users.models import ServiceUser
from academy.models import Item


class Order(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('invoice', 'Счёт для юридического лица'),
        ('card_online', 'Картой онлайн'),
    ]
    STATUS_CHOICES = [
        ('processing', 'Обрабатывается'),
        ('completed', 'Выполнен'),
        ('cancelled', 'Отменен'),
    ]
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        verbose_name='Способ оплаты',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Покупатель',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='processing',
        verbose_name='Статус',
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

    @property
    def total_price(self):
        total_price = sum(
            order_item.total_price for order_item in self.items.all())
        return total_price

    def __str__(self):
        return f"Заказ номер {self.id} для {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Заказ',
    )
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, verbose_name='Товар',)
    quantity = models.PositiveIntegerField(
        default=1, verbose_name='Количество',)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена',)

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    @property
    def total_price(self):
        total_price = self.quantity * self.item.price
        return total_price

    def __str__(self):
        return f"{self.quantity} x {self.item.title} in Order {self.order.id}"


class ShippingAddress(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя',)
    last_name = models.CharField(max_length=50, verbose_name='Фамилия',)
    email = models.EmailField(verbose_name='Почта',)
    phone = models.CharField(max_length=20, verbose_name='Телефон',)
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name='shipping_address', verbose_name='Заказ',)

    class Meta:
        verbose_name = 'Данные покупки'
        verbose_name_plural = 'Данные покупки'

    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'

    def __str__(self):
        return f"""
        Для: {self.first_name} {self.last_name},
        Почта: {self.email},
        Телефон: {self.phone}
        """
