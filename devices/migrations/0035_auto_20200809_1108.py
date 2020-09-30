# Generated by Django 2.2.10 on 2020-08-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0034_auto_20200809_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googlephone',
            name='google_capacity',
            field=models.CharField(blank=True, choices=[('4 GB', '4 GB'), ('8 GB', '8 GB'), ('16 GB', '16 GB'), ('32 GB', '32 GB'), ('64 GB', '64 GB'), ('128 GB SSD', '128GB SSD'), ('128 GB ', '128 GB '), ('256 GB', '256 GB'), ('256 GB SSD', '256 GB SSD'), ('512 GB', '512 GB'), ('512 GB SSD', '512 GB'), ('750 GB', '750 GB'), ('1 TB', '1 TB'), ('1.5 TB', '1.5 TB'), ('1 TB SSD', '1 TB SSD'), ('2 TB SSD', '2 TB SSD'), ('3 TB SSD', '3 TB SSD'), ('4 TB SSD', '4 TB SSD'), ('not known', "Don't Know")], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ipad',
            name='ipad_capacity',
            field=models.CharField(choices=[('4 GB', '4 GB'), ('8 GB', '8 GB'), ('16 GB', '16 GB'), ('32 GB', '32 GB'), ('64 GB', '64 GB'), ('128 GB SSD', '128GB SSD'), ('128 GB ', '128 GB '), ('256 GB', '256 GB'), ('256 GB SSD', '256 GB SSD'), ('512 GB', '512 GB'), ('512 GB SSD', '512 GB'), ('750 GB', '750 GB'), ('1 TB', '1 TB'), ('1.5 TB', '1.5 TB'), ('1 TB SSD', '1 TB SSD'), ('2 TB SSD', '2 TB SSD'), ('3 TB SSD', '3 TB SSD'), ('4 TB SSD', '4 TB SSD'), ('not known', "Don't Know")], default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='iphone',
            name='capacity',
            field=models.CharField(choices=[('4 GB', '4 GB'), ('8 GB', '8 GB'), ('16 GB', '16 GB'), ('32 GB', '32 GB'), ('64 GB', '64 GB'), ('128 GB SSD', '128GB SSD'), ('128 GB ', '128 GB '), ('256 GB', '256 GB'), ('256 GB SSD', '256 GB SSD'), ('512 GB', '512 GB'), ('512 GB SSD', '512 GB'), ('750 GB', '750 GB'), ('1 TB', '1 TB'), ('1.5 TB', '1.5 TB'), ('1 TB SSD', '1 TB SSD'), ('2 TB SSD', '2 TB SSD'), ('3 TB SSD', '3 TB SSD'), ('4 TB SSD', '4 TB SSD'), ('not known', "Don't Know")], default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='ipod',
            name='ipod_capacity',
            field=models.CharField(choices=[('4 GB', '4 GB'), ('8 GB', '8 GB'), ('16 GB', '16 GB'), ('32 GB', '32 GB'), ('64 GB', '64 GB'), ('128 GB SSD', '128GB SSD'), ('128 GB ', '128 GB '), ('256 GB', '256 GB'), ('256 GB SSD', '256 GB SSD'), ('512 GB', '512 GB'), ('512 GB SSD', '512 GB'), ('750 GB', '750 GB'), ('1 TB', '1 TB'), ('1.5 TB', '1.5 TB'), ('1 TB SSD', '1 TB SSD'), ('2 TB SSD', '2 TB SSD'), ('3 TB SSD', '3 TB SSD'), ('4 TB SSD', '4 TB SSD'), ('not known', "Don't Know")], default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='macbook',
            name='ram_capacity',
            field=models.CharField(blank=True, choices=[('4 GB', '4 GB'), ('8 GB', '8 GB'), ('16 GB', '16 GB'), ('32 GB', '32 GB'), ('64 GB', '64 GB'), ('128 GB SSD', '128GB SSD'), ('128 GB ', '128 GB '), ('256 GB', '256 GB'), ('256 GB SSD', '256 GB SSD'), ('512 GB', '512 GB'), ('512 GB SSD', '512 GB'), ('750 GB', '750 GB'), ('1 TB', '1 TB'), ('1.5 TB', '1.5 TB'), ('1 TB SSD', '1 TB SSD'), ('2 TB SSD', '2 TB SSD'), ('3 TB SSD', '3 TB SSD'), ('4 TB SSD', '4 TB SSD'), ('not known', "Don't Know")], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='macbook',
            name='storage_capacity',
            field=models.CharField(blank=True, choices=[('4 GB', '4 GB'), ('8 GB', '8 GB'), ('16 GB', '16 GB'), ('32 GB', '32 GB'), ('64 GB', '64 GB'), ('128 GB SSD', '128GB SSD'), ('128 GB ', '128 GB '), ('256 GB', '256 GB'), ('256 GB SSD', '256 GB SSD'), ('512 GB', '512 GB'), ('512 GB SSD', '512 GB'), ('750 GB', '750 GB'), ('1 TB', '1 TB'), ('1.5 TB', '1.5 TB'), ('1 TB SSD', '1 TB SSD'), ('2 TB SSD', '2 TB SSD'), ('3 TB SSD', '3 TB SSD'), ('4 TB SSD', '4 TB SSD'), ('not known', "Don't Know")], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='macbook',
            name='year',
            field=models.CharField(blank=True, choices=[('Mid 2012', 'Mid 2012'), ('Late 2012', 'Late 2012'), ('Early 2013', 'Early 2013'), ('Mid 2013', 'Mid 2013'), ('Late 2013', 'Late 2013'), ('Early 2014', 'Early 2014'), ('Mid 2014', 'Mid 2014'), ('Early 2015', 'Early 2015'), ('Mid 2015', 'Mid 2015'), ('Early 2016', 'Early 2016'), ('Late 2016', 'Late 2016'), ('2016', '2016'), ('2017', '2017'), ('Mid 2017', 'Mid 2017'), ('Mid 2018', 'Mid 2018'), ('Late 2018', 'Late 2018'), ('2019', '2019'), ('Mid 2019', 'Mid 2019'), ('2018', '2018'), ('2020', '2020')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='samsungphone',
            name='samsung_capacity',
            field=models.CharField(blank=True, choices=[('4 GB', '4 GB'), ('8 GB', '8 GB'), ('16 GB', '16 GB'), ('32 GB', '32 GB'), ('64 GB', '64 GB'), ('128 GB SSD', '128GB SSD'), ('128 GB ', '128 GB '), ('256 GB', '256 GB'), ('256 GB SSD', '256 GB SSD'), ('512 GB', '512 GB'), ('512 GB SSD', '512 GB'), ('750 GB', '750 GB'), ('1 TB', '1 TB'), ('1.5 TB', '1.5 TB'), ('1 TB SSD', '1 TB SSD'), ('2 TB SSD', '2 TB SSD'), ('3 TB SSD', '3 TB SSD'), ('4 TB SSD', '4 TB SSD'), ('not known', "Don't Know")], default=None, max_length=30, null=True),
        ),
    ]