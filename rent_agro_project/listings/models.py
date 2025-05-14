from django.db import models
from accounts.models import CustomUser

class Listing(models.Model):
    # Определяем выбор типов техники
    EQUIPMENT_TYPES = (
        ('tractor', 'Трактор'),
        ('combine', 'Комбайн'),
        ('seeder', 'Сеялка'),
        ('plow', 'Плуг'),
    )

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Владелец")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")
    equipment_type = models.CharField(max_length=50, choices=EQUIPMENT_TYPES, verbose_name="Тип техники")
    power = models.IntegerField(verbose_name="Мощность (л.с.)", null=True, blank=True)
    region = models.CharField(max_length=100, verbose_name="Регион")
    image = models.ImageField(upload_to='equipment/', verbose_name="Фото", null=True, blank=True)
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона", blank=True, null=True)
    telegram_username = models.CharField(max_length=50, verbose_name="Telegram username", blank=True)
    instagram_username = models.CharField(max_length=50, verbose_name="Instagram username", blank=True)

    def __str__(self):
        return self.title
