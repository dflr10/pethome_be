from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):

    # Creates and saves a User with the given email and password.
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Creates and saves a superuser with the given email and password.
    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id_user = models.BigAutoField(primary_key=True)
    username = models.CharField(
        'username', max_length=45, unique=True, null=False)
    password = models.CharField('Password', max_length=250, null=False)
    name = models.CharField('Name', max_length=45, null=False)
    email = models.CharField('Email', max_length=45, null=False)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'
