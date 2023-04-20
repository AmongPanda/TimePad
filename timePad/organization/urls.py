from django.urls import path
from .views import *


urlpatterns = [
    path('event/', Event, name='event'),
    path('user/', UserOrg, name='user'),
    path('ticket/', Ticket, name='ticket')
]