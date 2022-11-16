# Generated by Django 4.0 on 2022-11-08 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(max_length=35, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='actor_id',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director_id',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='quality',
        ),
        migrations.CreateModel(
            name='MovieQuality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quality', to='movie.movie')),
                ('quality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movie.quality')),
            ],
        ),
        migrations.CreateModel(
            name='MovieComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movie.comment')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movie.movie')),
            ],
        ),
    ]