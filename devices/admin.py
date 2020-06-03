from django.contrib import admin
from .models import Iphone,Macbook,Ipad

class IphoneAdmin(admin.ModelAdmin):
    list_display = ('iphone_model','carrier','capacity','Offer')
    list_filter = ('iphone_model', 'capacity', 'carrier',)
    search_field =('iphone_model', 'capacity', 'carrier',)

class MacbookAdmin(admin.ModelAdmin):
    list_display = ('Macbook_Model','Screen_Size','year','offer')
    list_filter = ('Macbook_Model','Screen_Size','year','offer')
    search_field =('Macbook_Model','Screen_Size','year','offer',)

class IpadAdmin(admin.ModelAdmin):
    list_display = ('ipad_model','ipad_generation','ipad_capacity','ipad_screensize','offer')
    list_filter = ('ipad_model','ipad_generation','ipad_capacity','ipad_screensize','offer')
    search_field =('ipad_model','ipad_generation','ipad_capacity','ipad_screensize','offer')

admin.site.register(Iphone, IphoneAdmin)
admin.site.register(Macbook, MacbookAdmin)
admin.site.register(Ipad, IpadAdmin)
