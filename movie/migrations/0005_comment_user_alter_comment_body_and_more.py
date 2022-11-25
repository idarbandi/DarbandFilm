# Generated by Django 4.0 on 2022-11-23 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_myuser_profile_pic'),
        ('movie', '0004_moviequality_download_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='user.myuser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(max_length=12000, null=True),
        ),
        migrations.AlterField(
            model_name='moviequality',
            name='Download_links',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]