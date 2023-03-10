# Generated by Django 4.0 on 2022-11-26 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='created_time',
            field=models.DateField(default='1401-09-05'),
        ),
        migrations.AddField(
            model_name='account',
            name='expired',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='modified_time',
            field=models.DateField(default='1401-09-05'),
        ),
    ]
