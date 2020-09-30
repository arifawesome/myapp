# Generated by Django 2.2.10 on 2020-07-24 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0022_auto_20200722_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airpods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airpods_model', models.CharField(blank=True, choices=[('Airpods Pro', 'Airpods Pro'), ('Airpods 2', 'Airpods 2'), ('Airpods', 'Airpods')], default=0, max_length=30, null=True)),
                ('charging_case', models.CharField(blank=True, choices=[('Wireless charging case', 'Wireless charging case'), ('Wired charging case', 'Wired charging case'), ('Don’t have idea', 'Don’t have idea')], default=0, max_length=3, null=True)),
                ('airpods_condition', models.CharField(blank=True, choices=[('Broken', 'Broken'), ('Fair', 'Fair'), ('GooD', 'Good'), ('Flawless', 'Flawless')], default=0, max_length=300, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SellBulk',
        ),
    ]