# Generated by Django 5.1 on 2024-10-21 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('villa', '0007_villamodel_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='villamodel',
            name='details',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
