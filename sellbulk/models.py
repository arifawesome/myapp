from django.db import models

# Create your models here.
class Devices(models.Model):
  
    deviceOrder=models.IntegerField(blank=True,null=True)
    deviceType=models.CharField(max_length=30,null=True)
    deviceCondition=models.CharField(max_length=30,null=True)
    deviceQuantity=models.IntegerField(blank=True,null=True)
        
    

    def __str__(self):
        return '%d: %s %s %d' % (self.deviceOrder, self.deviceType, self.deviceCondition, self.deviceQuantity)

class Inquerer(models.Model):
    firstName=models.CharField(max_length=30,null=True)
    lastName=models.CharField(max_length=30,null=True)
    email=models.EmailField()
    companyOrganization=models.CharField(max_length=30,null=True)
    phoneNumber=models.CharField(max_length=30,null=True)
    additionalInfo=models.CharField(max_length=30,null=True)
    devices=models.ManyToManyField(Devices,)
    def __str__(self):
        return '%s %s' % (self.firstName, self.email)