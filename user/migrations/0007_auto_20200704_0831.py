# Generated by Django 3.0.6 on 2020-07-04 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200704_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertradeinfo',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='user.UserInfo'),
        ),
    ]
