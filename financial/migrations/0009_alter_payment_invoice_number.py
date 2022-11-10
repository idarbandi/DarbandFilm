# Generated by Django 4.0 on 2022-11-10 10:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0008_alter_payment_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='invoice_number',
            field=models.UUIDField(default=uuid.UUID('7ca27585-42e0-41a5-b058-9ab1267245a0'), unique=True, verbose_name='invoice number'),
        ),
    ]
