from django.contrib import admin

# Register your models here.
from .models import UserAddress,UserInfo,UserTradeInfo,UserDevicesInfo,UserPaymentInfo
#UserOrder

# Register your models here.
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user','addressType','addressLine1','addressLine2','city','state','zipcode','primaryAddress')
    list_filter = ('user','addressType','addressLine1','addressLine2','city','state','zipcode','primaryAddress')
    search_field =('user','addressType','addressLine1','addressLine2','city','state','zipcode','primaryAddress')


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user','phoneNumber','secondary_email',)
    list_filter = ('user','phoneNumber','secondary_email',)
    search_field = ('user','phoneNumber','secondary_email',)

class UserTradeInfoAdmin(admin.ModelAdmin):
    list_display = ('user','orderNo','status','address','orderDate','lableSent','shippingLableReceived','deviceReceived','deviceReview','deviceAccepted','deviceAcceptanceComment','paymentMethod')
    list_filter = ('user','orderNo','status','address','orderDate','lableSent','shippingLableReceived','deviceReceived','deviceReview','deviceAccepted','deviceAcceptanceComment','paymentMethod')
    search_field = ('user','orderNo','status','address','orderDate','lableSent','shippingLableReceived','deviceReceived','deviceReview','deviceAccepted','deviceAcceptanceComment','paymentMethod')

'''class UserOrderAdmin(admin.ModelAdmin):
    list_display = ('userinfo',)
    list_filter = ('userinfo',)
    search_field = ('userinfo',)'''

class UserDevicesInfoAdmin(admin.ModelAdmin):
    list_display = ('trade','deviceType','deviceModel','deviceCapacity','deviceCarrier','deviceCondition','deviceYear','deviceProcessor','deviceOffer','deviceGeneration','deviceSize','deviceEdition','deviceBand','deviceEngraving')

    list_filter = ('trade','deviceType','deviceModel','deviceCapacity','deviceCarrier','deviceCondition','deviceYear','deviceProcessor','deviceOffer','deviceGeneration','deviceSize','deviceEdition','deviceBand','deviceEngraving')
    search_field = ('trade','deviceType','deviceModel','deviceCapacity','deviceCarrier','deviceCondition','deviceYear','deviceProcessor','deviceOffer','deviceGeneration','deviceSize','deviceEdition','deviceBand','deviceEngraving')

class UserPaymentInfoAdmin(admin.ModelAdmin):
    list_display = ('paymentMethod','name','username','Phone','email')

    list_filter = ('paymentMethod','name','username','Phone','email')
    search_field = ('paymentMethod','name','username','Phone','email')

admin.site.register(UserAddress,UserAddressAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(UserTradeInfo, UserTradeInfoAdmin)
admin.site.register(UserPaymentInfo, UserPaymentInfoAdmin)
admin.site.register(UserDevicesInfo, UserDevicesInfoAdmin)