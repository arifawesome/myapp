# Generated by Django 3.0.6 on 2020-06-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0007_auto_20200602_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macbook',
            name='Screen_Size',
            field=models.CharField(choices=[('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16')], default=0, max_length=30),
        ),
    ]
