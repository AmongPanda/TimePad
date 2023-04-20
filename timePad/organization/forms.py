from django import forms
from .models import *

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'age', 'date_time', 'buration', 'price', 'description_event', 'mini_description_event',
                  'image', 'organizer']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['name_ticket', 'name_participants', 'description_ticket', 'image_ticket', 'price_ticket',
                  'email_participants']

class UserOrgForm(forms.Form):
    class Meta:
        model = UserOrg
        field = ['user', 'phone_number', 'address', 'age_user', 'event']