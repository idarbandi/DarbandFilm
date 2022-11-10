# Generated by Django 4.0 on 2022-11-10 09:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0007_alter_payment_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='invoice_number',
            field=models.UUIDField(default=uuid.UUID('d2f1dede-4b18-46d9-8c2d-d055fa54c1e2'), unique=True, verbose_name='invoice number'),
        ),
    ]
