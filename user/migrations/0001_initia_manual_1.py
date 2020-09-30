# Generated by Django 2.2.10 on 2020-07-26 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestUserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30, null=True)),
                ('lastName', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('companyOrganization', models.CharField(max_length=30, null=True)),
                ('phoneNumber', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GuestUserOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userorder', to='user.GuestUserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addressType', models.CharField(max_length=30, null=True)),
                ('addressLine1', models.CharField(max_length=30, null=True)),
                ('addressLine2', models.CharField(max_length=30, null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('state', models.CharField(max_length=30, null=True)),
                ('zipcode', models.CharField(max_length=30, null=True)),
                ('primaryAddress', models.BooleanField(default=False, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useraddress', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserTradeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNo', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('status', models.CharField(choices=[('completed', 'completed'), ('In-Progress', 'In-Progress')], max_length=30, null=True)),
                ('orderDate', models.DateTimeField(auto_now=True)),
                ('lableSent', models.DateField(blank=True, null=True)),
                ('shippingLableReceived', models.DateField(blank=True, null=True)),
                ('deviceReceived', models.DateField(blank=True, null=True)),
                ('deviceReview', models.CharField(blank=True, choices=[('Ok', 'ok'), ('Requoted', 'Requoted')], default=None, max_length=30, null=True)),
                ('deviceAccepted', models.CharField(blank=True, choices=[('yes', 'yes'), ('Customer Denied', 'Customer Denied'), ('No', 'No'), ('Other', 'Other')], default=None, max_length=30, null=True)),
                ('deviceAcceptanceComment', models.CharField(blank=True, max_length=300, null=True)),
                ('totalPayment', models.CharField(blank=True, max_length=30, null=True)),
                ('paymentMethod', models.CharField(blank=True, choices=[('check', 'check'), ('Paypal', 'Paypal'), ('Amazon Gift Card', 'Amazon Gift Card'), ('Cash', 'Cash')], max_length=30, null=True)),
                ('paymentReferenceNo', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceShippingMethod', models.CharField(choices=[('local-pickup', 'local-pickup'), ('USPS', 'USPS'), ('FedEx', 'FedEx'), ('UPS', 'UPS')], max_length=30, null=True)),
                ('deviceTrackingInbound', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceTrackingOutbound', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderaddress', to='user.UserAddress')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='userorder', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secondary_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userinfo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDevicesInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceType', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceModel', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceCapacity', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceCarrier', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceCondition', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceYear', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceProcessor', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceOffer', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceGeneration', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceSize', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceEdition', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceBand', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceEngraving', models.CharField(blank=True, max_length=30, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='user.UserTradeInfo')),
            ],
        ),
        migrations.CreateModel(
            name='GuestUserTradeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tradeReferenceNo', models.CharField(max_length=30, null=True)),
                ('status', models.CharField(choices=[('completed', 'completed'), ('In-Progress', 'In-Progress')], max_length=30, null=True)),
                ('orderDate', models.DateField(blank=True, null=True)),
                ('lableSent', models.DateField(blank=True, null=True)),
                ('shippingLableReceived', models.DateField(blank=True, null=True)),
                ('deviceReceived', models.DateField(blank=True, null=True)),
                ('deviceReview', models.CharField(blank=True, choices=[('Ok', 'ok'), ('Requoted', 'Requoted')], default=None, max_length=30, null=True)),
                ('deviceAccepted', models.CharField(blank=True, choices=[('yes', 'yes'), ('Customer Denied', 'Customer Denied'), ('No', 'No'), ('Other', 'Other')], default=None, max_length=30, null=True)),
                ('deviceAcceptanceComment', models.CharField(blank=True, max_length=300, null=True)),
                ('paymentMethod', models.CharField(blank=True, choices=[('check', 'check'), ('Paypal', 'Paypal'), ('Amazon Gift Card', 'Amazon Gift Card'), ('Cash', 'Cash')], max_length=30, null=True)),
                ('paymentReferenceNo', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceShippingMethod', models.CharField(choices=[('local-pickup', 'local-pickup'), ('USPS', 'USPS'), ('FedEx', 'FedEx'), ('UPS', 'UPS')], max_length=30, null=True)),
                ('deviceTrackingInbound', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceTrackingOutbound', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guestuseraddresses', to='user.UserAddress')),
                ('userorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usertrade', to='user.GuestUserOrder')),
            ],
        ),
        migrations.CreateModel(
            name='GuestUserDevicesInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceType', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceModel', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceCapacity', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceCarrier', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceCondition', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceYear', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceProcessor', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceOffer', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceGeneration', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceSize', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceEdition', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceBand', models.CharField(blank=True, max_length=30, null=True)),
                ('deviceEngraving', models.CharField(blank=True, max_length=30, null=True)),
                ('usertradeinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usertradeinfo', to='user.GuestUserTradeInfo')),
            ],
        ),
        migrations.CreateModel(
            name='GuestUserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addressType', models.CharField(max_length=30, null=True)),
                ('addressLine1', models.CharField(max_length=30, null=True)),
                ('addressLine2', models.CharField(max_length=30, null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('state', models.CharField(max_length=30, null=True)),
                ('zipcode', models.CharField(max_length=30, null=True)),
                ('userinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useraddress', to='user.GuestUserInfo')),
            ],
        ),
    ]
