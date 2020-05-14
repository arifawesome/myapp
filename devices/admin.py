from django.contrib import admin
from .models import Iphone

class IphoneAdmin(admin.ModelAdmin):
    list_display = ()



admin.site.register(Iphone, IphoneAdmin)

