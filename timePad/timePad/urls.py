from django.contrib import admin
from django.urls import path
from organization.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event/', events, name='event'),
    path('user/', user_org, name='user'),
    path('ticket/', tickets, name='ticket')
]
