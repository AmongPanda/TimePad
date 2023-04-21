from django.contrib import admin
from django.urls import path
from organization.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('event/', events, name='event'),
    path('user/', user_org, name='user'),
    path('ticket/', tickets, name='ticket'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]
