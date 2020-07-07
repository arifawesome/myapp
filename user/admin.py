from django.contrib import admin
from .models import UserInfo,UserTradeInfo,UserAddress
# Register your models here.
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('addressLine1','city','state',)
    list_filter = ('addressLine1','city','state',)
    search_field =('addressLine1','city','state',)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('phoneNumber','secondary_email','user')
    list_filter = ('phoneNumber','secondary_email','user')
    search_field =('phoneNumber','secondary_email','user')


class UserTradeInfoAdmin(admin.ModelAdmin):
    list_display = ('tradeReferenceNo','status','deviceReview','paymentMethod','address')
    list_filter = ('tradeReferenceNo','status','deviceReview','paymentMethod')
    search_field = ('tradeReferenceNo','status','deviceReview','paymentMethod')

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(UserTradeInfo, UserTradeInfoAdmin)
admin.site.register(UserAddress, UserAddressAdmin)