from django.contrib import admin
from .models import UserInfo,UserTradeInfo
# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('phoneNumber','city','state','user')
    list_filter = ('phoneNumber','city','state')
    search_field =('phoneNumber','city','state')




class UserTradeInfoAdmin(admin.ModelAdmin):
    list_display = ('tradeReferenceNo','status','deviceReview','paymentMethod','address')
    list_filter = ('tradeReferenceNo','status','deviceReview','paymentMethod')
    search_field = ('tradeReferenceNo','status','deviceReview','paymentMethod')

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(UserTradeInfo, UserTradeInfoAdmin)