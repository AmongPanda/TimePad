from django.urls import path, include
from .views import *
from .views import add_event


urlpatterns = [
    path('', main, name='main'),
    path('add_event/', add_event, name='add_event')
]