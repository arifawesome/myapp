# Generated by Django 2.2.10 on 2020-08-02 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0031_auto_20200730_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='samsungphone',
            name='samsung_screenburn',
            field=models.CharField(blank=True, choices=[('Yes', 'yes'), ('No%', 'no')], default=None, max_length=30, null=True),
        ),
    ]
