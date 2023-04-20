# Generated by Django 4.1.7 on 2023-04-20 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Название мероприятия')),
                ('description', models.TextField(null=True, verbose_name='Описание мероприятия')),
                ('date', models.DateTimeField(null=True, verbose_name='Дата и время мероприятия')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Стоимость участия в мероприятии')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Название билета')),
                ('description', models.TextField(null=True, verbose_name='Описание билета')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Цена билета')),
                ('tariff', models.CharField(max_length=50, null=True, verbose_name='Тариф билета')),
            ],
        ),
        migrations.CreateModel(
            name='UserOrg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, null=True, verbose_name='Ссылка на стандартную модель пользователя')),
                ('phone_number', models.CharField(max_length=20, null=True, verbose_name='Номер телефона пользователя')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='Адрес пользователя')),
                ('age_user', models.IntegerField(default=0, null=True, verbose_name='Возраст пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.userorg', verbose_name='Пользователь, зарегистрированный на мероприятие')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.event', verbose_name='Мероприятие, на которое зарегистрирован пользователь')),
                ('ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.ticket', verbose_name='Билет, на который зарегистрирован пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='tickets',
            field=models.ManyToManyField(null=True, to='organization.ticket', verbose_name='Доступные билеты для мероприятия'),
        ),
    ]
