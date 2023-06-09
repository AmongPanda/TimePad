# Generated by Django 4.1.7 on 2023-04-21 02:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_alter_event_options_alter_ticket_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userorg',
            old_name='address',
            new_name='adress',
        ),
        migrations.AddField(
            model_name='event',
            name='age',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Возрастной ценз'),
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
