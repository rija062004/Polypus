# Generated by Django 5.1.1 on 2024-09-30 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('nomCompletClient', models.CharField(max_length=50, verbose_name='Nom')),
                ('telephoneClient', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True, verbose_name='Téléphone')),
                ('emailClient', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('adresseClient', models.CharField(max_length=50, verbose_name='Adresse')),
                ('interestedClient', models.CharField(max_length=32, verbose_name='intérer')),
                ('fonctionClient', models.CharField(max_length=32, verbose_name='Fonction')),
                ('employerContacter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employer.employermodel', verbose_name='Employer concerner')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]
