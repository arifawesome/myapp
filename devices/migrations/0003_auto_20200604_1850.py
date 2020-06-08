# Generated by Django 3.0.6 on 2020-06-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_iphone_condition'),
    ]

    operations = [
        migrations.CreateModel(
            name='SamsungPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('samsung_model', models.CharField(choices=[('Galaxy Z-Flip', 'Galaxyzflip'), ('Galaxy Fold SM-F900', 'Galaxyfoldsmf900'), ('Galaxy Note 10+ SM-N975', 'Galaxynote10Plussmn975'), ('Galaxy Note 10 SM-N970', 'Galaxynote10Smn970'), ('Galaxy S10+', 'Galaxys10Plus'), ('Galaxy S10', 'Galaxys10'), ('Galaxy S10e', 'Galaxys10E'), ('Galaxy Note 9 SM-N960', 'Galaxynote9Smn960'), ('Galaxy S9+ SM-G965A', 'Galaxys9Plussmg965A'), ('Galaxy S9 SM-G960A', 'Galaxys9Smg960A'), ('Galaxy S8+ SM-G955A', 'Galaxys8Plussmg955A'), ('GalaxyS8SMG950A', 'Galaxys8Smg950A'), ('Galaxy S8 Active SM-G892A', 'Galaxys8Activesmg892A'), ('Galaxy Note 8 SM-N950A', 'Galaxynote8Smn950A'), ('Galaxy S7 edge SM-G935A', 'Galaxys7Edgesmg935A'), ('Galaxy S7 SM-G930A', 'Galaxys7Smg930A'), ('Galaxy S6 edge+ SM-G928', 'Galaxys6Edgeplussmg928A'), ('Galaxy S6 Edge SM-G925V', 'Galaxys6Edgesmg925V'), ('Galaxy S20', 'Galaxys20'), ('Galaxy S20 Ultra', 'Galaxys20Ultra'), ('Galaxy S20+', 'Galaxys20Plus')], default=0, max_length=30)),
                ('samsung_capacity', models.CharField(choices=[('16 GB', '16 GB'), ('32 GB', '32 GB'), ('64 GB', '64 GB'), ('128 GB', '128 GB'), ('256 GB', '256 GB'), ('512 GB', '512 GB'), ('750 GB', '750 GB'), ('1 TB', '1 TB'), ('2 TB', '2 TB'), ('3 TB', '3 TB'), ('4 TB', '4 TB')], default=0, max_length=30)),
                ('samsung_carrier', models.CharField(choices=[('att', 'AT&T'), ('verizon', 'Verizon'), ('tmobile', 'Tmobile'), ('sprint', 'Sprint'), ('unlocked', 'Factory Unlocked'), ('other', 'Other'), ('wifi', 'Wifi')], default=None, max_length=30)),
                ('samsung_condition', models.CharField(choices=[('Broken', 'Broken'), ('30%', '30%'), ('50%', '50%'), ('75%', '75%'), ('100%', '100%')], default=None, max_length=30)),
                ('offer', models.CharField(default=0, max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='macbook',
            name='other',
            field=models.CharField(blank=True, choices=[('1.1Ghz i3', '1.1Ghz i3'), ('1.1Ghz i5', '1.1Ghz i5'), ('Dedicated Graphics', 'Dedicated Graphics'), ('Retina', 'Retina'), ('No Retina', 'No Retina'), ('Touch Vega', 'Touch Vega'), ('Touch', 'Touch')], default=0, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='macbook',
            name='Processer',
            field=models.CharField(choices=[('1.1Ghz', '1.1Ghz'), ('1.1Ghz i3', '1.1Ghz i3'), ('1.1Ghz i5', '1.1Ghz i5'), ('1.2Ghz', '1.2Ghz'), ('1.3Ghz', '1.3Ghz'), ('1.4Ghz', '1.4Ghz'), ('1.6Ghz', '1.6Ghz'), ('1.7Ghz', '1.7Ghz'), ('1.8Ghz', '1.8Ghz'), ('2.0Ghz', '2.0Ghz'), ('2.2Ghz', '2.2Ghz'), ('2.3Ghz', '2.3Ghz'), ('2.30Ghz', '2.30Ghz'), ('2.4Ghz', '2.4Ghz'), ('2.5Ghz', '2.5Ghz'), ('2.6Ghz', '2.6Ghz'), ('2.60Ghz', '2.60Ghz'), ('2.7Ghz', '2.7Ghz'), ('2.8Ghz', '2.8Ghz'), ('2.9Ghz', '2.9Ghz'), ('3.0Ghz', '3.0Ghz'), ('3.1Ghz', '3.1Ghz'), ('3.3Ghz', '3.3Ghz'), ('3.5Ghz', '3.5Ghz')], default=0, max_length=30),
        ),
    ]