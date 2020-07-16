from django.contrib import admin

# Register your models here.
from .models import UserAddress,UserInfo,UserOrder,UserTradeInfo

# Register your models here.
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('userinfo','addressType','addressLine1','addressLine2','city','state','zipcode','primaryAddress')
    list_filter = ('userinfo','addressType','addressLine1','addressLine2','city','state','zipcode','primaryAddress')
    search_field =('userinfo','addressType','addressLine1','addressLine2','city','state','zipcode','primaryAddress')


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user','phoneNumber','secondary_email',)
    list_filter = ('user','phoneNumber','secondary_email',)
    search_field = ('user','phoneNumber','secondary_email',)

class UserTradeInfoAdmin(admin.ModelAdmin):
    list_display = ('userorder','tradeReferenceNo','status','address','orderDate','lableSent','shippingLableReceived','deviceReceived','deviceReview','deviceAccepted','deviceAcceptanceComment','paymentMethod')
    list_filter = ('userorder','tradeReferenceNo','status','address','orderDate','lableSent','shippingLableReceived','deviceReceived','deviceReview','deviceAccepted','deviceAcceptanceComment','paymentMethod')
    search_field = ('userorder','tradeReferenceNo','status','address','orderDate','lableSent','shippingLableReceived','deviceReceived','deviceReview','deviceAccepted','deviceAcceptanceComment','paymentMethod')

class UserOrderAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user',)
    search_field = ('user',)


admin.site.register(UserAddress,UserAddressAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(UserTradeInfo, UserTradeInfoAdmin)
admin.site.register(UserOrder, UserOrderAdmin)