from django.contrib import admin
from .models import Contact_us

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'date']
    class Meta:
        model = Contact_us
# Register your models here.
admin.site.register(Contact_us,ContactAdmin)