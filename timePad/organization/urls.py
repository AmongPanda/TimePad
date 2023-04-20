from django.urls import path
from .views import *


urlpatterns = [
    path('event/', add_event, name='event')
]