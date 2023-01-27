# Generated by Django 4.0 on 2023-01-06 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_comment_created_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('file', models.FilePathField()),
                ('summary', models.TextField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default='1401-10-16 12:04:12.281073'),
        ),
    ]
