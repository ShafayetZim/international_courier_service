# Generated by Django 4.0.5 on 2023-01-17 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0003_about_benefit_facility_gallery_partner_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.ImageField(blank=True, upload_to='service'),
        ),
    ]