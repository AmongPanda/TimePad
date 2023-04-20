from django.urls import path
from .views import *


urlpatterns = [
    path('event/', events, name='event'),
    path('user/', user_org, name='user'),
    path('ticket/', tickets, name='ticket')
]