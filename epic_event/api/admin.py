from django.contrib import admin

from epic_event.api.models import Contract, Event, User


class AdminSite(admin.AdminSite):
    site_header = "Admin Epic Event"


admin_site = AdminSite(name="Admin")


class UserAdmin(admin.ModelAdmin):
    pass


class ContractAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


admin_site.register(User, UserAdmin)
admin_site.register(Contract, ContractAdmin)
admin_site.register(Event, EventAdmin)
