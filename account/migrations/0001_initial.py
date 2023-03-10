# Generated by Django 4.0 on 2022-11-08 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration', models.PositiveSmallIntegerField(null=True)),
                ('package', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='account', to='package.package')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='user.myuser')),
            ],
        ),
    ]
