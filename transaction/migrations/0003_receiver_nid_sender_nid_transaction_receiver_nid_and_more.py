# Generated by Django 4.0.5 on 2022-11-16 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_transaction_barcode_transaction_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiver',
            name='nid',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sender',
            name='nid',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='receiver_nid',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='shipper_nid',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
