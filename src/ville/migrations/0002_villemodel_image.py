# Generated by Django 5.1 on 2024-10-14 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ville', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='villemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]