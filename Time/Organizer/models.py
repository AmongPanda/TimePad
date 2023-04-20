from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name='Название билета')  # Название билета
    description = models.TextField(null=True, verbose_name='Описание билета')  # Описание билета
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, verbose_name='Цена билета')  # Цена билета
    has_online_streaming = models.BooleanField(default=False, null=True, verbose_name='Доступ к онлайн-трансляция')  # Есть ли онлайн-трансляция
    has_access_to_talks = models.BooleanField(default=False, null=True, verbose_name='Доступ к докладам')  # Есть ли доступ к докладам
    has_access_to_workshops = models.BooleanField(default=False, null=True, verbose_name='Доступ к мастер-классам')  # Есть ли доступ к мастер-классам
    has_lunch = models.BooleanField(default=False, null=True, verbose_name='Доступ к обеду')  # Включен ли обед
    tariff = models.CharField(max_length=50, null=True, verbose_name='Тариф билета')  # Тариф билета


class Event(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name='Название мероприятия')  # Название мероприятия
    description = models.TextField(null=True, verbose_name='Описание мероприятия')  # Описание мероприятия
    date = models.DateTimeField(null=True, verbose_name='Дата и время мероприятия')  # Дата и время мероприятия
    cost = models.DecimalField(max_digits=6, decimal_places=2, null=True, verbose_name='Стоимость участия в мероприятии')  # Стоимость участия в мероприятии
    invoice_count = models.PositiveIntegerField(default=0, null=True, verbose_name='Кол-во выставленных счетов на оплату билетов')  # Количество выставленных счетов на оплату билетов
    tickets = models.ManyToManyField(Ticket, null=True, verbose_name='Доступные билеты для мероприятия')  # Доступные билеты для мероприятия
    ticket_count_online_streaming = models.PositiveIntegerField(default=0, null=True, verbose_name='Кол-во купленных билетов на онлайн-трансляцию')  # Количество купленных билетов на онлайн-трансляцию
    ticket_count_access_to_talks = models.PositiveIntegerField(default=0, null=True, verbose_name='Кол-во купленных билетов на доступ к докладам')  # Количество купленных билетов на доступ к докладам
    ticket_count_access_to_workshops = models.PositiveIntegerField(default=0, null=True, verbose_name='Кол-во купленных билетов на доступ к мастер-классам')  # Количество купленных билетов на доступ к мастер-классам

    def increment_ticket_count_online_streaming(self):
        self.ticket_count_online_streaming += 1
        self.save()

    def increment_ticket_count_access_to_talks(self):
        self.ticket_count_access_to_talks += 1
        self.save()

    def increment_ticket_count_access_to_workshops(self):
        self.ticket_count_access_to_workshops += 1
        self.save()

    def get_available_tickets(self):
        return self.tickets.all()  # Получаем список доступных

    def get_available_tickets(self):
        return self.tickets.all()  # Получаем список доступных билетов для мероприятия

class Discount(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name='Название скидки')  # Название скидки
    discount_value = models.DecimalField(max_digits=6, decimal_places=2, null=True, verbose_name='Размер скидки')  # Размер скидки
    max_uses = models.PositiveIntegerField(null=True, blank=True,  verbose_name='Максимальное кол-во использований скидки')  # Максимальное количество использований скидки
    start_date = models.DateTimeField(null=True, blank=True,  verbose_name='Дата начала действия скидки')  # Дата начала действия скидки
    end_date = models.DateTimeField(null=True, blank=True,  verbose_name='Дата окончания действия скидки')  # Дата окончания действия скидки
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, verbose_name='Билет, к которому применяется скидка')  # Билет, к которому применяется скидка
class UserOrg(models.Model):
    name = models.CharField(max_length=20, null=True, verbose_name='Ссылка на стандартную модель пользователя') # Ссылка на стандартную модель пользователя Django
    phone_number = models.CharField(max_length=20, null=True, verbose_name='Номер телефона пользователя') # Номер телефона пользователя
    address = models.CharField(max_length=200, null=True, verbose_name='Адрес пользователя') # Адрес пользователя
    age_user = models.IntegerField(default=0, null=True, verbose_name='Возраст пользователя') #Возраст пользователя
class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, verbose_name='Мероприятие, на которое зарегистрирован пользователь')  # Мероприятие, на которое зарегистрирован пользователь
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, verbose_name='Билет, на который зарегистрирован пользователь')  # Билет, на который зарегистрирован пользователь
    customer = models.ForeignKey(UserOrg, on_delete=models.CASCADE, null=True, verbose_name='Пользователь, зарегистрированный на мероприятие')  # Пользователь, зарегистрированный на мероприятие
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Скидка, примененная к билету')  # Скидка, примененная к билету

    def apply_discount(self):
        if self.discount:
            self.ticket.price -= self.discount.discount_value  # Применяем скидку к цене билета
            self.ticket.save()



  
