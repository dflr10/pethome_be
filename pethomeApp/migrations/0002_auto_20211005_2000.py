# Generated by Django 3.2.7 on 2021-10-06 01:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pethomeApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='address',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='birdday_aprox',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='city',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='post_date',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='user_type',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='tel',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
        migrations.AddField(
            model_name='pet',
            name='bday_aprox',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='bday_aprox'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='date_register',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_register'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=0, max_length=45, unique=True, verbose_name='username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=models.CharField(max_length=250, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=45, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=45, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=46, verbose_name='Password'),
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]
