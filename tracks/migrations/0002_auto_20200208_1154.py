# Generated by Django 2.0 on 2020-02-08 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackplaylist',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracks.Track'),
        ),
    ]
