# Generated by Django 5.1 on 2024-10-21 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('villa', '0006_alter_villamodel_lotvilla'),
    ]

    operations = [
        migrations.AddField(
            model_name='villamodel',
            name='details',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
