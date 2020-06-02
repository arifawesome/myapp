from django.db import models

# Create your models here.
CONDITION_CHOICES = (
        ("YES", "YES"),
        ("NO", "NO"),
    )
PROCESSOR_CHOICES = (
       ("1.1Ghz","1.1Ghz"),
        ("1.2Ghz","1.2Ghz"),
        ("1.3Ghz","1.3Ghz"),
        ("1.4Ghz","1.4Ghz"),
        ("1.6Ghz","1.6Ghz"),
       ("1.7Ghz","1.7Ghz"),
        ("1.8Ghz","1.8Ghz"),
        ("2.0Ghz","2.0Ghz"),
        ("2.2Ghz","2.2Ghz"),
        ("2.3Ghz","2.3Ghz"),
        ("2.30Ghz","2.30Ghz"),
        ("2.4Ghz","2.4Ghz"),
        ("2.5Ghz","2.5Ghz"),
        ("2.6Ghz","2.6Ghz"),
        ("2.60Ghz","2.60Ghz"),
        ("2.7Ghz","2.7Ghz"),
        ("2.8Ghz","2.8Ghz"),
        ("2.9Ghz","2.9Ghz"),
        ("3.0Ghz","3.0Ghz"),
        ("3.1Ghz","3.1Ghz"),
        ("3.3Ghz","3.3Ghz"),
       ("3.5Ghz","3.5Ghz"),
    )

SCREEN_CHOICES =(
    ("11","11"),
    ("12","12"),
    ("13","13"),
    ("14","14"),
    ("15","15"),
    ("16","16"),
    
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
    iphone_model = models.CharField(choices=IphoneModel.choices,max_length=30,default=0)

    class Carrier(models.TextChoices):
        att='AT&T'
        verizon='Verizon'
        tmobile='Tmobile'
        sprint='Sprint'
        unlocked='Factory Unlocked'
        other='Other'
    carrier =models.CharField(choices=Carrier.choices,max_length=30,default=None)

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

    capacity = models.CharField(choices=Capacity.choices, max_length=30,default=None)

    Power_On=models.CharField(max_length = 3,choices =CONDITION_CHOICES,default=None)
        #Power_Off='device power off'

    Screen_Lightup=models.CharField(max_length = 3,choices =CONDITION_CHOICES,default=None)
        #Screen_Not_Lightup='device screen doesn\'t fully lightup'

    Device_Works=models.CharField(max_length = 3,choices =CONDITION_CHOICES,default=None)
        #Device_Not_Works='Device is not fully funcational'


    Scratches=models.CharField(max_length = 3,choices =CONDITION_CHOICES,default=None)
        #No_Scratches = 'There are not any scratches on device'

    Crack=models.CharField(max_length = 3,choices =CONDITION_CHOICES,default=None)
       #No_Crack = 'there are no any cracks on device'
        #condition = models.CharField(choices=Condition.choices, max_length=50)
    Offer=models.CharField(max_length = 3,default=0)

    def __str__(self):
        return str(self.iphone_model) + " " + str(self.capacity) + " " +str(self.carrier)

class Macbook(models.Model):
    class MacbookModel(models.TextChoices):
        MB ="Macbook"
        MBA = "Macbook Air"
        MBP ="MAcbook Pro"

    Macbook_Model=models.CharField(choices=MacbookModel.choices,max_length=30,default=0)

    class ScreenSize(models.TextChoices):
       ''' Eleven="11\""
        Thirteen="13\""
        Fifteen="15\""
        Sixteen="16\""
        Seventeen="17\""'''

    Screen_Size=models.CharField(choices=SCREEN_CHOICES,max_length=30,default=0)

    '''class Processor(models.TextChoices):
        oneone="1.1Ghz"
        onetwo="1.2Ghz"
        onethree="1.3Ghz"
        onefour="1.4Ghz"
        onesix="1.6Ghz"
        oneseven="1.7Ghz"
        oneeight="1.8Ghz"
        twozero="2.0Ghz"
        twotwo="2.2Ghz"
        twothree="2.3Ghz"
        twothirty="2.30Ghz"
        twofour="2.4Ghz"
        twofive="2.5Ghz"
        twosix="2.6Ghz"
        twosixty="2.60Ghz"
        twoseven="2.7Ghz"
        twoeight="2.8Ghz"
        twonine="2.9Ghz"
        threezero="3.0Ghz"
        threeone="3.1Ghz"
        threethree="3.3Ghz"
        threefive="3.5Ghz" '''

    Processer=models.CharField(choices=PROCESSOR_CHOICES,max_length=30,default=0)

    class Year(models.TextChoices):
        Mid12="Mid 2012"
        Late12="Late 2012"
        Early13="Early 2013"
        Mid13="Mid 2013"
        Late13="Late 2013"
        Early14="Early 2014"
        Mid14="Mid 2014"
        Early15="Early 2015"
        Mid15="Mid 2015"
        Early16="Early 2016"
        Late16="Late 2016"
        Mid17="Mid 2017"
        Mid18="Mid 2018"
        Late18="Late 2018"
        year2019="2019"
        Mid19="Mid 2019"
        year2020="2020"

    year=models.CharField(choices=Year.choices,max_length=30,default=0)


    class CosmeticCondition(models.TextChoices):
        Broken="Broken"
        Fair="Fair"
        Good="Good"
        Flawless="Flawless"
    
    Cosmetic_condition=models.CharField(choices=CosmeticCondition.choices,max_length=30,default=0)

    offer=models.CharField(max_length=3,default=0)