# Generated by Django 4.2.1 on 2023-05-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_southafricaupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='southafricaupdate',
            name='southAfricaupdate',
            field=models.ImageField(upload_to='southafricaupdatepicture/'),
        ),
    ]
