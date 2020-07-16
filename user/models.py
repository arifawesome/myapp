from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS_CHOICES=(
    ('completed','completed'),
    ('In-Progress','In-Progress')
)
DEVICE_REVIEW_CHOICES=(
    ('Ok','ok' ),
    ('Requoted','Requoted'),
)
PAYMENT_CHOICES=(
    ('check','check' ),
    ('Paypal','Paypal' ),
    ('Amazon Gift Card', 'Amazon Gift Card' ),
    ('Cash','Cash' ),
 )
SHIPPING_CHOICES=(
    ('local-pickup','local-pickup' ),
    ('USPS','USPS' ),
    ('FedEx', 'FedEx' ),
    ('UPS','UPS' ),
 )
ACCEPTANCE_CHOICES=(
    ('yes','yes' ),
    ('Customer Denied','Customer Denied' ),
    ('No', 'No' ),
    ('Other','Other' ),
 )


class UserInfo(models.Model):
    user=models.ForeignKey('auth.User', related_name='userinfo', on_delete=models.CASCADE)
    secondary_email=models.EmailField(blank=True,null=True)
    phoneNumber=models.CharField(max_length=20,null=True,blank=True)
    
    def __str__(self):
        return str(self.user) 

class UserAddress(models.Model):
    userinfo=models.ForeignKey(UserInfo,related_name='useraddress',on_delete=models.CASCADE)
    addressType=models.CharField(max_length=30,null=True)
    addressLine1=models.CharField(max_length=30,null=True)
    addressLine2=models.CharField(max_length=30,null=True)
    city=models.CharField(max_length=30,null=True)
    state=models.CharField(max_length=30,null=True)
    zipcode=models.CharField(max_length=30,null=True)
    primaryAddress=models.BooleanField(default=False,null=True)


    def __str__(self):
        return str(self.addressType)+ " " +str(self.addressLine1)+ " " +str(self.addressLine2)+ " "+str(self.city)+ " "+str(self.state)+ " "+str(self.zipcode)+ " "+str(self.primaryAddress)

class UserOrder(models.Model):
    user=models.ForeignKey('auth.User', related_name='userorder', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) 

class UserTradeInfo(models.Model):
    userorder=models.ForeignKey(UserOrder,related_name='usertrade',on_delete=models.CASCADE)
    tradeReferenceNo=models.CharField(max_length=30,null=True)
    status=models.CharField(choices=STATUS_CHOICES,max_length=30,null=True)
    address=models.ForeignKey(UserAddress,related_name='addresses',on_delete=models.CASCADE, null=True, blank=True)
    orderDate=models.DateField(null=True,blank=True)
    lableSent=models.DateField(null=True,blank=True)
    shippingLableReceived=models.DateField(null=True,blank=True)
    deviceReceived=models.DateField(null=True,blank=True)
    deviceReview=models.CharField(choices=DEVICE_REVIEW_CHOICES,max_length=30,null=True,default=None,blank=True)
    deviceAccepted=models.CharField(choices=ACCEPTANCE_CHOICES,max_length=30,null=True,default=None,blank=True)
    deviceAcceptanceComment=models.CharField(max_length=300,blank=True,null=True)
    paymentMethod=models.CharField(choices=PAYMENT_CHOICES,max_length=30,null=True,blank=True)
    paymentReferenceNo=models.CharField(max_length=30,blank=True,null=True)
    deviceShippingMethod=models.CharField(choices=SHIPPING_CHOICES,max_length=30,null=True)
    deviceTrackingInbound=models.CharField(max_length=30,blank=True,null=True)
    deviceTrackingOutbound=models.CharField(max_length=30,blank=True,null=True)
