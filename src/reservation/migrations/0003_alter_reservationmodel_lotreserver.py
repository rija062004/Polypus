# Generated by Django 5.1 on 2024-10-17 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_reservationmodel_lotreserver'),
        ('villaUnique', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='lotReserver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='villaUnique.villaunique', verbose_name='Lotissement choisi'),
        ),
    ]
