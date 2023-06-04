# Generated by Django 4.2.1 on 2023-05-31 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_rename_carrier_shipmentdetails_current_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerPictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('bannerpictures1', models.ImageField(upload_to='bannerpictures/')),
                ('bannerpictures2', models.ImageField(upload_to='bannerpictures/')),
                ('bannerpictures3', models.ImageField(upload_to='bannerpictures/')),
            ],
        ),
    ]
