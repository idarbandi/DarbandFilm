# Generated by Django 4.0 on 2022-11-24 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_comment_user_alter_comment_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movie.movie'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='MovieComments',
        ),
    ]
