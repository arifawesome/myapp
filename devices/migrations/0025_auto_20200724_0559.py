# Generated by Django 2.2.10 on 2020-07-24 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0024_auto_20200724_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airpods',
            name='airpods_condition',
            field=models.CharField(blank=True, choices=[('Broken', 'Broken'), ('Fair', 'Fair'), ('GooD', 'Good'), ('Flawless', 'Flawless')], default=0, max_length=30, null=True),
        ),
    ]
