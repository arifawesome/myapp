# Generated by Django 3.0.6 on 2020-06-09 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0012_devices_img_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devices',
            old_name='img_url',
            new_name='imagePath',
        ),
    ]