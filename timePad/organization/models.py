from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name='Название билета')  # Название билета
    description = models.TextField(null=True, verbose_name='Описание билета')  # Описание билета
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, verbose_name='Цена билета')  # Цена билета
    tariff = models.CharField(max_length=50, null=True, verbose_name='Тариф билета')  # Тариф билета


class Event(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name='Название мероприятия')  # Название мероприятия
    description = models.TextField(null=True, verbose_name='Описание мероприятия')  # Описание мероприятия
    date = models.DateTimeField(null=True, verbose_name='Дата и время мероприятия')  # Дата и время мероприятия
    tickets = models.ForeignKey(Ticket, on_delete=models.CASCADE,null=True, verbose_name='Доступные билеты для мероприятия')  # Доступные билеты для мероприятия



# class Discount(models.Model):
#     name = models.CharField(max_length=200, null=True, verbose_name='Название скидки')  # Название скидки
#     discount_value = models.DecimalField(max_digits=6, decimal_places=2, null=True, verbose_name='')  # Размер скидки
#     max_uses = models.PositiveIntegerField(null=True, blank=True,
#                                            verbose_name='Максимальное кол-во использований скидки')  # Максимальное количество использований скидки
#     start_date = models.DateTimeField(null=True, blank=True,
#                                       verbose_name='Дата начала действия скидки')  # Дата начала действия скидки
#     end_date = models.DateTimeField(null=True, blank=True,
#                                     verbose_name='Дата окончания действия скидки')  # Дата окончания действия скидки
#     ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True,
#                                verbose_name='Билет, к которому применяется скидка')  # Билет, к которому применяется скидка


class UserOrg(models.Model):
    user = models.CharField(max_length=20, null=True,
                                verbose_name='Имя')  # Ссылка на стандартную модель пользователя Django
    phone_number = models.CharField(max_length=20, null=True,
                                    verbose_name='Номер телефона пользователя')  # Номер телефона пользователя
    address = models.CharField(max_length=200, null=True, verbose_name='Адрес пользователя')  # Адрес пользователя
    age_user = models.IntegerField(default=0, null=True, verbose_name='Возраст пользователя')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, verbose_name='Выбери мероприятие')







