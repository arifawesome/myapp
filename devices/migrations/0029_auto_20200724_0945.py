# Generated by Django 2.2.10 on 2020-07-24 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0028_airpods_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='iwatch',
            name='iwatch_box',
            field=models.CharField(blank=True, choices=[('Yes', 'yes'), ('No%', 'no')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='googlephone',
            name='google_carrier',
            field=models.CharField(choices=[('att', 'AT&T'), ('verizon', 'Verizon'), ('tmobile', 'Tmobile'), ('sprint', 'Sprint'), ('unlocked', 'Factory Unlocked'), ('other', 'Other'), ('not known', "Don't Know"), ('wifi', 'Wifi'), ('wifi Only', 'Wifi Only'), ('GPS', 'GPS'), ('GPS + Cellular', 'GPS + Cellular')], default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='ipad',
            name='ipad_carrier',
            field=models.CharField(choices=[('att', 'AT&T'), ('verizon', 'Verizon'), ('tmobile', 'Tmobile'), ('sprint', 'Sprint'), ('unlocked', 'Factory Unlocked'), ('other', 'Other'), ('not known', "Don't Know"), ('wifi', 'Wifi'), ('wifi Only', 'Wifi Only'), ('GPS', 'GPS'), ('GPS + Cellular', 'GPS + Cellular')], default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='iphone',
            name='carrier',
            field=models.CharField(choices=[('att', 'AT&T'), ('verizon', 'Verizon'), ('tmobile', 'Tmobile'), ('sprint', 'Sprint'), ('unlocked', 'Factory Unlocked'), ('other', 'Other'), ('not known', "Don't Know"), ('wifi', 'Wifi'), ('wifi Only', 'Wifi Only'), ('GPS', 'GPS'), ('GPS + Cellular', 'GPS + Cellular')], default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='iwatch',
            name='iwatch_band',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('Sport Band-Any Color', 'Sport Band-Any Color'), ('Sport Loop-Any Color', 'Sport Loop-Any Color'), ('Nylon Band-Any Color', 'Nylon Band-Any Color'), ('Milanese Loop', 'Milanese loop'), ('Classic Buckle', 'Classic Buckle'), ('Leather Loop', 'Leather Loop'), ('Modern Buckle', 'Modern Buckle'), ('Hermes Band', 'Hermes Band'), ('Link Bracelet', 'Link Bracelet'), ('Gold Buckle-Any Band', 'Gold Buckle-Any Band'), ('No Band', 'No Band')], default=0, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='iwatch',
            name='iwatch_carrier',
            field=models.CharField(blank=True, choices=[('att', 'AT&T'), ('verizon', 'Verizon'), ('tmobile', 'Tmobile'), ('sprint', 'Sprint'), ('unlocked', 'Factory Unlocked'), ('other', 'Other'), ('not known', "Don't Know"), ('wifi', 'Wifi'), ('wifi Only', 'Wifi Only'), ('GPS', 'GPS'), ('GPS + Cellular', 'GPS + Cellular')], default=0, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='iwatch',
            name='iwatch_condition',
            field=models.CharField(blank=True, choices=[('Broken', 'Broken'), ('Working%', 'Working'), ('30%', '30%'), ('50%', '50%'), ('75%', '75%'), ('100%', '100%')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='iwatch',
            name='iwatch_edition_casing',
            field=models.CharField(blank=True, choices=[('Aluminium Case', 'Aluminium Case'), ('Regular-Steel Case', 'Regular-Steel Case'), ('Hermes-Steel Case', 'Hermes-Steel Case'), ('Stainless-Steel Case', 'Stainless-Steel Case'), ('Titanium Case', 'Titanium Case'), ('Ceramic Case', 'Ceramic Case'), ('Nike+ -Aluminium Case', 'Nike+ -Aluminium Case')], default=0, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='iwatch',
            name='iwatch_functional',
            field=models.CharField(blank=True, choices=[('Yes', 'yes'), ('No%', 'no')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='iwatch',
            name='iwatch_model',
            field=models.CharField(choices=[('Apple Watch Original(1st Gen)', 'Apple Watch Original(1st Gen)'), ('Apple Watch Series 1', 'Apple Watch Series 1'), ('Apple Watch Series 2', 'Apple Watch Series 2'), ('Apple Watch Series 3', 'Apple Watch Series 3'), ('Apple Watch Series 4', 'Apple Watch Series 4'), ('Apple Watch Series 5', 'Apple Watch Series 5')], default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='iwatch',
            name='iwatch_powercord',
            field=models.CharField(blank=True, choices=[('Yes', 'yes'), ('No%', 'no')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='iwatch',
            name='iwatch_size',
            field=models.CharField(blank=True, choices=[('38mm', '38mm'), ('40mm', '40mm'), ('42mm', '42mm'), ('44mm', '44mm')], default=0, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='samsungphone',
            name='samsung_carrier',
            field=models.CharField(choices=[('att', 'AT&T'), ('verizon', 'Verizon'), ('tmobile', 'Tmobile'), ('sprint', 'Sprint'), ('unlocked', 'Factory Unlocked'), ('other', 'Other'), ('not known', "Don't Know"), ('wifi', 'Wifi'), ('wifi Only', 'Wifi Only'), ('GPS', 'GPS'), ('GPS + Cellular', 'GPS + Cellular')], default=None, max_length=30),
        ),
    ]
