# Generated by Django 4.1.7 on 2023-08-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/CustomerProfilePic/'),
        ),
    ]
