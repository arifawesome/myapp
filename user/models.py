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
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phoneNumber=models.CharField(max_length=30,null=True)
    addressLine1=models.CharField(max_length=30,null=True)
    addressLine2=models.CharField(max_length=30,null=True)
    city=models.CharField(max_length=30,null=True)
    state=models.CharField(max_length=30,null=True)
    zipcode=models.CharField(max_length=30,null=True)
    primaryAddress=models.BooleanField(default=False,null=True)

    def __str__(self):
        return str(self.user)

class UserTradeInfo(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    tradeReferenceNo=models.CharField(max_length=30)
    status=models.CharField(choices=STATUS_CHOICES,max_length=30,null=True)
    address=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    orderDate=models.DateField()
    lableSent=models.DateField()
    lableReceived=models.DateField()
    deviceReceived=models.DateField()
    deviceReview=models.CharField(choices=DEVICE_REVIEW_CHOICES,max_length=30,null=True)
    deviceAccepted=models.CharField(choices=ACCEPTANCE_CHOICES,max_length=30,null=True)
    deviceAcceptanceComment=models.CharField(max_length=300,blank=True)
    paymentMethod=models.CharField(choices=PAYMENT_CHOICES,max_length=30,null=True)
    paymentReferenceNo=models.CharField(max_length=30,blank=True)
    deviceShippingMethod=models.CharField(choices=SHIPPING_CHOICES,max_length=30,null=True)
    deviceTrackingInbound=models.CharField(max_length=30,blank=True)
    deviceTrackingOutbound=models.CharField(max_length=30,blank=True)




    

