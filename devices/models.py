from django.db import models

# Create your models here.
CONDITION_CHOICES = (
        ("YES", "YES"),
        ("NO", "NO"),
    )
class Iphone(models.Model):
    class IphoneModel(models.TextChoices):
        iphone11PM='IPhone 11 Pro Max'
        iphone11P='Iphone 11 Pro'
        iphone11='Iphone 11'
        iphoneXSM='Iphone XS Max '
        iphoneXS='Iphone XS '
        iphoneXR='Iphone XR'
        iphoneX='Iphone X'
        iphone8P='Iphone 8 Plus'
        iphone8='Iphone 8'
        iphone7P='Iphone 7 Plus'
        iphone6SP='Iphone 6S Plus'
        iphone6S='Iphone 6s'
        iphone6='Iphone 6'
        iphoneSE2='Iphone SE 2nd Gen'
        iphoneSE='Iphone SE'
    iphone_model = models.CharField(choices=IphoneModel.choices,max_length=30)

    class Carrier(models.TextChoices):
        att='AT&T'
        verizon='Verizon'
        tmobile='Tmobile'
        sprint='Sprint'
        unlocked='Factory Unlocked'
        other='Other'
    carrier =models.CharField(choices=Carrier.choices,max_length=30)

    class Capacity(models.Choices):
        sixteen='16 GB'
        thiry_two='32 GB'
        sixty_four='64 GB'
        one_twenty_eight='128 GB'
        two_fifty_six ='256 GB'
        five_twelve= '512 GB'
        one_tb='1 TB'
        two_tb='2 TB'
        four_tb='4 TB'

    capacity = models.CharField(choices=Capacity.choices, max_length=30)

    Power_On=models.CharField(max_length = 3,choices =CONDITION_CHOICES)
        #Power_Off='device power off'

    Screen_Lightup=models.CharField(max_length = 3,choices =CONDITION_CHOICES)
        #Screen_Not_Lightup='device screen doesn\'t fully lightup'

    Device_Works=models.CharField(max_length = 3,choices =CONDITION_CHOICES)
        #Device_Not_Works='Device is not fully funcational'


    Scratches=models.CharField(max_length = 3,choices =CONDITION_CHOICES)
        #No_Scratches = 'There are not any scratches on device'

    Crack=models.CharField(max_length = 3,choices =CONDITION_CHOICES)
       #No_Crack = 'there are no any cracks on device'
        #condition = models.CharField(choices=Condition.choices, max_length=50)