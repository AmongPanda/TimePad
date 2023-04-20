from django.contrib import admin
from .models import *


class TicketAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    pass

class DiscountAdmin(admin.ModelAdmin):
    pass

class RegistrationAdmin(admin.ModelAdmin):
    pass

class RegistrationAdmin(admin.ModelAdmin):
    pass

class UserOrgAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(UserOrg, UserOrgAdmin)