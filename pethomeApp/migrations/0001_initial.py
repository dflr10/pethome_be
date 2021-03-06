# Generated by Django 3.2.7 on 2021-10-02 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id_user', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, verbose_name='name')),
                ('lastname', models.CharField(max_length=45, verbose_name='lastname')),
                ('email', models.EmailField(max_length=45, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=46, verbose_name='password')),
                ('tel', models.CharField(max_length=45, verbose_name='tel')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id_user_type', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id_pet', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, verbose_name='name')),
                ('specie', models.CharField(max_length=45, verbose_name='specie')),
                ('breed', models.CharField(max_length=45, null=True, verbose_name='breed')),
                ('birdday_aprox', models.DateTimeField(verbose_name='birdday_aprox')),
                ('post_date', models.DateTimeField(verbose_name='post_date')),
                ('description', models.TextField(max_length=250, verbose_name='description')),
                ('image', models.ImageField(upload_to='pethomeApp/static/images/pets', verbose_name='image')),
                ('address', models.TextField(max_length=45, verbose_name='address')),
                ('city', models.CharField(max_length=45, verbose_name='city')),
                ('state', models.BooleanField(default=True, verbose_name='state')),
                ('id_user', models.ForeignKey(max_length=45, on_delete=django.db.models.deletion.CASCADE, related_name='id_user_pet', to=settings.AUTH_USER_MODEL)),
                ('user_type', models.ForeignKey(max_length=45, on_delete=django.db.models.deletion.CASCADE, related_name='user_type_pet', to='pethomeApp.usertype')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(max_length=45, on_delete=django.db.models.deletion.CASCADE, related_name='user_type_user', to='pethomeApp.usertype'),
        ),
    ]
