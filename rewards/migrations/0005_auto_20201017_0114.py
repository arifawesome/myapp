# Generated by Django 2.2.10 on 2020-10-17 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewards', '0004_auto_20201016_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewards',
            name='bonus',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='rewards',
            name='condition',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='rewards',
            name='description',
            field=models.CharField(blank=True, max_length=130, null=True),
        ),
        migrations.AlterField(
            model_name='rewards',
            name='discount',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]