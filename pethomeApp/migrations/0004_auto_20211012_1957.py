# Generated by Django 3.2.7 on 2021-10-13 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pethomeApp', '0003_auto_20211006_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='gender',
            field=models.CharField(default=0, max_length=45, verbose_name='gender'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=250, verbose_name='Password'),
        ),
    ]