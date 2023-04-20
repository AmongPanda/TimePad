from django import forms
from .models import *
from django.forms.widgets import DateInput


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'tickets']
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['name', 'description', 'price', 'tariff']


class UserOrgForm(forms.ModelForm):
    class Meta:
        model = UserOrg
        fields = ['user', 'phone_number', 'adress', 'age_user', 'event']
