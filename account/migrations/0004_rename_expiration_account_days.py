# Generated by Django 4.0 on 2022-11-26 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_remaining_days'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='expiration',
            new_name='days',
        ),
    ]
