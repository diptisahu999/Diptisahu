# Generated by Django 4.0.6 on 2022-11-08 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_patient'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Docter',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
