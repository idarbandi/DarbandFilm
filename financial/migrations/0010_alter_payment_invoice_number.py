# Generated by Django 4.0 on 2022-11-10 10:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0009_alter_payment_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='invoice_number',
            field=models.UUIDField(default=uuid.UUID('83688578-5d81-4cd9-b521-61406a155e0d'), unique=True, verbose_name='invoice number'),
        ),
    ]
