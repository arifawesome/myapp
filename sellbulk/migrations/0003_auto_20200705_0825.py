# Generated by Django 3.0.6 on 2020-07-05 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellbulk', '0002_auto_20200705_0822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devices',
            options={'ordering': ['deviceOrder']},
        ),
        migrations.AlterUniqueTogether(
            name='devices',
            unique_together={('inquerer', 'deviceOrder')},
        ),
    ]
