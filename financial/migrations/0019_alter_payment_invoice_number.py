# Generated by Django 4.0 on 2023-01-06 13:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0018_alter_payment_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='invoice_number',
            field=models.UUIDField(default=uuid.UUID('18767fde-611b-4700-b34e-729a62459839'), unique=True, verbose_name='invoice number'),
        ),
    ]