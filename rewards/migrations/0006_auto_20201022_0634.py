# Generated by Django 2.2.10 on 2020-10-22 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rewards', '0005_auto_20201017_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrewards',
            name='promocode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rewards.Rewards'),
        ),
    ]