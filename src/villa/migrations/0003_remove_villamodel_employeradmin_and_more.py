# Generated by Django 5.1 on 2024-10-04 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('villa', '0002_alter_villamodel_employeradmin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='villamodel',
            name='employerAdmin',
        ),
        migrations.RemoveField(
            model_name='villamodel',
            name='prixVilla',
        ),
        migrations.RemoveField(
            model_name='villamodel',
            name='villeVilla',
        ),
    ]