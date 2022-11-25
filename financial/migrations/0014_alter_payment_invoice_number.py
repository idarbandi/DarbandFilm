# Generated by Django 4.0 on 2022-11-23 10:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0013_alter_payment_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='invoice_number',
            field=models.UUIDField(default=uuid.UUID('2af860c7-ec78-4d7a-8f7c-2bcee39007b6'), unique=True, verbose_name='invoice number'),
        ),
    ]
