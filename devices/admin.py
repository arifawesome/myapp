from django.contrib import admin
from .models import Iphone,Macbook,Ipad, SamsungPhone, GooglePhone,Ipod,Iwatch, Devices,SellBulk
from import_export.admin import ImportExportModelAdmin

@admin.register(Iphone)
class IphoneAdmin(ImportExportModelAdmin):
    pass
    list_display = ('iphone_model','carrier','capacity','Offer')
    list_filter = ('iphone_model', 'capacity', 'carrier',)
    search_field =('iphone_model', 'capacity', 'carrier',)

'''class IphoneAdmin(admin.ModelAdmin):
    list_display = ('iphone_model','carrier','capacity','Offer')
    list_filter = ('iphone_model', 'capacity', 'carrier',)
    search_field =('iphone_model', 'capacity', 'carrier',)'''

class MacbookAdmin(admin.ModelAdmin):
    list_display = ('Macbook_Model','Screen_Size','year','offer')
    list_filter = ('Macbook_Model','Screen_Size','year','offer')
    search_field =('Macbook_Model','Screen_Size','year','offer',)

class IpadAdmin(admin.ModelAdmin):
    list_display = ('ipad_model','ipad_generation','ipad_capacity','ipad_screensize','offer')
    list_filter = ('ipad_model','ipad_generation','ipad_capacity','ipad_screensize','offer')
    search_field =('ipad_model','ipad_generation','ipad_capacity','ipad_screensize','offer')

class SamsungphoneAdmin(admin.ModelAdmin):
    list_display = ('samsung_model','samsung_capacity','samsung_carrier','offer')
    list_filter = ('samsung_model','samsung_capacity','samsung_carrier','offer')
    search_field =('samsung_model','samsung_capacity','samsung_carrier','offer')

class GooglephoneAdmin(admin.ModelAdmin):
    list_display = ('google_model','google_capacity','google_carrier','offer')
    list_filter = ('google_model','google_capacity','google_carrier','offer')
    search_field =('google_model','google_capacity','google_carrier','offer')

class IpodAdmin(admin.ModelAdmin):
    list_display = ('ipod_model','ipod_capacity','offer','ipod_generation')
    list_filter = ('ipod_model','ipod_capacity','offer','ipod_generation')
    search_field =('ipod_model','ipod_capacity','offer','ipod_generation')

class IwatchAdmin(admin.ModelAdmin):
    list_display = ('iwatch_model','iwatch_carrier','iwatch_size','offer')
    list_filter = ('iwatch_model','iwatch_carrier','iwatch_size','offer')
    search_field =('iwatch_model','iwatch_carrier','iwatch_size','offer')

class DevicesAdmin(admin.ModelAdmin):
    list_display = ('device','info')

class SellBulkAdmin(admin.ModelAdmin):
    list_display = ('device','quantity', 'contact_info')

admin.site.register(Macbook, MacbookAdmin)
admin.site.register(Ipad, IpadAdmin)
admin.site.register(SamsungPhone, SamsungphoneAdmin)
admin.site.register(GooglePhone, GooglephoneAdmin)
admin.site.register(Ipod, IpodAdmin)
admin.site.register(Iwatch, IwatchAdmin)
admin.site.register(Devices, DevicesAdmin)
admin.site.register(SellBulk, SellBulkAdmin)

