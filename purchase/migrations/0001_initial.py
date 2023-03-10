# Generated by Django 4.0 on 2022-11-07 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('package', '0001_initial'),
        ('financial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveBigIntegerField()),
                ('status', models.SmallIntegerField(choices=[(10, 'Paid'), (-10, 'Not Paid')], default=-10)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now_add=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='package.package')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='purchase', to='financial.payment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='user.myuser')),
            ],
        ),
    ]
