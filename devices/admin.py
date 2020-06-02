from django.contrib import admin
from .models import Iphone,Macbook

class IphoneAdmin(admin.ModelAdmin):
    list_display = ('iphone_model','carrier','capacity','Offer')
    list_filter = ('iphone_model', 'capacity', 'carrier',)
    search_field =('iphone_model', 'capacity', 'carrier',)

class MacbookAdmin(admin.ModelAdmin):
    list_display = ('Macbook_Model','Screen_Size','year','offer')
    list_filter = ('Macbook_Model','Screen_Size','year','offer')
    search_field =('Macbook_Model','Screen_Size','year','offer',)




admin.site.register(Iphone, IphoneAdmin)
admin.site.register(Macbook, MacbookAdmin)
