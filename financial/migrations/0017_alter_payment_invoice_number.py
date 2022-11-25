# Generated by Django 4.0 on 2022-11-24 11:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0016_alter_payment_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='invoice_number',
            field=models.UUIDField(default=uuid.UUID('a8a5f53d-a91d-4fdd-8d0c-2e36d79d39c2'), unique=True, verbose_name='invoice number'),
        ),
    ]