from django.db import models

# Create your models here.

    
class Inquerer(models.Model):
    firstName=models.CharField(max_length=30,null=True)
    lastName=models.CharField(max_length=30,null=True)
    email=models.EmailField()
    companyOrganization=models.CharField(max_length=30,null=True)
    phoneNumber=models.CharField(max_length=30,null=True)
    additionalInfo=models.CharField(max_length=30,null=True)
   
    def __str__(self):
        return str(self.firstName )+ " " + str(self.lastName )+ " " + str(self.email )
   
class Devices(models.Model):
    inquerer=models.ForeignKey(Inquerer, related_name='devices', on_delete=models.CASCADE)
    deviceOrder=models.IntegerField(blank=True,null=True)
    deviceType=models.CharField(max_length=30,null=True)
    deviceCondition=models.CharField(max_length=30,null=True)
    deviceQuantity=models.IntegerField(blank=True,null=True)
        
    
