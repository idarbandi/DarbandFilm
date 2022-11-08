# Generated by Django 4.0 on 2022-11-07 14:26

from django.db import migrations, models
import django.db.models.deletion
import khayyam.jalali_date


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=48)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True)),
                ('days', models.PositiveSmallIntegerField()),
                ('is_enable', models.BooleanField(default=True)),
                ('is_golden', models.BooleanField(default=False)),
                ('created_day', models.DateField(default=khayyam.jalali_date.JalaliDate.today)),
                ('created_time', models.TimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=25)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benefits', to='package.package')),
            ],
        ),
    ]
