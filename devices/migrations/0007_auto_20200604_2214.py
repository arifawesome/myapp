# Generated by Django 3.0.6 on 2020-06-04 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0006_ipod_ipod_generation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iwatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iwatch_model', models.CharField(choices=[('Apple Watch Original', 'Applewatchoriginal'), ('Apple Watch Series 1', 'Applewatchseries1'), ('Apple Watch Series 2', 'Applewatchseries2'), ('Apple Watch Series 3', 'Applewatchseries3'), ('Apple Watch Series 4', 'Applewatchseries4'), ('Apple Watch Series 5', 'Applewatchseries5')], default=0, max_length=30)),
                ('iwatch_carrier', models.CharField(choices=[('att', 'AT&T'), ('verizon', 'Verizon'), ('tmobile', 'Tmobile'), ('sprint', 'Sprint'), ('unlocked', 'Factory Unlocked'), ('other', 'Other'), ('wifi', 'Wifi'), ('wifi Only', 'Wifi Only'), ('wifi + Cellular', 'wifi + Cellular')], default=0, max_length=30)),
                ('iwatch_edition_casing', models.CharField(choices=[('Sport-Aluminium Case', 'Sport-Aluminium case'), ('Regular-Steel Case', 'Regular-Steel Case'), ('Hermes-Steel Case', 'Hermes-Steel Case'), ('Edition-Steel Case', 'Edition-Steel Case'), ('Edition-Titanium Case', 'Edition-Titanium Case'), ('Edition-Ceramic Case', 'Edition-Ceramic Case'), ('Nike+ -Aluminium Case', 'Nike+ -Aluminium Case')], default=0, max_length=30)),
                ('iwatch_size', models.CharField(choices=[('38mm', '38mm'), ('40mm', '40mm'), ('42mm', '42mm'), ('44mm', '44mm')], default=0, max_length=30)),
                ('iwatch_band', models.CharField(choices=[('Sport Band-Any Color', 'Sport Band-Any Color'), ('Nylon Band-Any Color', 'Nylon Band-Any Color'), ('Milanese Loop', 'Milanese loop'), ('Classic Buckle', 'Classic Buckle'), ('Leather Loop', 'Leather Loop'), ('Modern Buckle', 'Modern Buckle'), ('Hermes Band', 'Hermes Band'), ('Link Bracelet', 'Link Bracelet'), ('Gold Buckle-Any Band', 'Gold Buckle-Any Band')], default=0, max_length=30)),
                ('iwatch_condition', models.CharField(choices=[('Broken', 'Broken'), ('Working%', 'Working'), ('30%', '30%'), ('50%', '50%'), ('75%', '75%'), ('100%', '100%')], default=None, max_length=30)),
                ('offer', models.CharField(default=0, max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='googlephone',
            name='google_carrier',
            field=models.CharField(choices=[('att', 'AT&T'), ('verizon', 'Verizon'), ('tmobile', 'Tmobile'), ('sprint', 'Sprint'), ('unlocked', 'Factory Unlocked'), ('other', 'Other'), ('wifi', 'Wifi'), ('wifi Only', 'Wifi Only'), ('wifi + Cellular', 'wifi + Cellular')], default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='ipad',
            name='ipad_carrier',
            field=models.CharField(choices=[('att', 'AT&T'), ('verizon', 'Verizon'), ('tmobile', 'Tmobile'), ('sprint', 'Sprint'), ('unlocked', 'Factory Unlocked'), ('other', 'Other'), ('wifi', 'Wifi'), ('wifi Only', 'Wifi Only'), ('wifi + Cellular', 'wifi + Cellular')], default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='iphone',
            name='carrier',
            field=models.CharField(choices=[('att', 'AT&T'), ('verizon', 'Verizon'), ('tmobile', 'Tmobile'), ('sprint', 'Sprint'), ('unlocked', 'Factory Unlocked'), ('other', 'Other'), ('wifi', 'Wifi'), ('wifi Only', 'Wifi Only'), ('wifi + Cellular', 'wifi + Cellular')], default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='samsungphone',
            name='samsung_carrier',
            field=models.CharField(choices=[('att', 'AT&T'), ('verizon', 'Verizon'), ('tmobile', 'Tmobile'), ('sprint', 'Sprint'), ('unlocked', 'Factory Unlocked'), ('other', 'Other'), ('wifi', 'Wifi'), ('wifi Only', 'Wifi Only'), ('wifi + Cellular', 'wifi + Cellular')], default=None, max_length=30),
        ),
    ]