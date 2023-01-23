# Generated by Django 4.0.5 on 2023-01-18 10:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0004_alter_service_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='slider')),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='detail',
            field=ckeditor.fields.RichTextField(),
        ),
    ]