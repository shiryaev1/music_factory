# Generated by Django 2.0 on 2020-02-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0003_auto_20200204_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='music',
            field=models.FileField(upload_to='media/upload_tracks/'),
        ),
    ]
