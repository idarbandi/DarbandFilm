# Generated by Django 4.0 on 2022-11-10 09:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0004_alter_payment_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='invoice_number',
            field=models.UUIDField(default=uuid.UUID('9f3025fc-4b68-443a-b119-4909aa6bec98'), unique=True, verbose_name='invoice number'),
        ),
    ]