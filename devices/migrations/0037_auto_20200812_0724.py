# Generated by Django 2.2.10 on 2020-08-12 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0036_auto_20200812_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macbook',
            name='macbook_model',
            field=models.CharField(choices=[('Macbook', 'Macbook'), ('Macbook Air', 'Macbook Air'), ('Macbook Pro', 'Macbook Pro')], default=0, max_length=30),
        ),
    ]