# Generated by Django 2.2.10 on 2020-10-09 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201009_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestuserdevicesinfo',
            name='trade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='user.GuestUserTradeInfo'),
        ),
    ]