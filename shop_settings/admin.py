from django.contrib import admin
from .models import Ttings

class TtingsAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email', 'address', 'facebook', 'insta', 'twit', 'linkedin']
    
    class Meta:
        model = Ttings
# Register your models here.
admin.site.register(Ttings,TtingsAdmin)