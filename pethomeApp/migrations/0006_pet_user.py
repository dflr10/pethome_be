# Generated by Django 3.2.7 on 2021-10-28 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pethomeApp', '0005_auto_20211025_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='user',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.CASCADE, to='pethomeApp.user'),
            preserve_default=False,
        ),
    ]
