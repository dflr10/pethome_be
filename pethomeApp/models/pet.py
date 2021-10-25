from django.db import models


class Pet(models.Model):
    id_pet = models.AutoField(primary_key=True)
    name = models.CharField('name', max_length=45, null=False)
    specie = models.CharField('specie', max_length=45, null=False)
    breed = models.CharField('breed', max_length=45, null=True)
    gender = models.CharField('gender', max_length=45, null=False)
    bday_aprox = models.DateField('bday_aprox', null=False)
    date_register = models.DateField('date_register', null=False)
    avaliable = models.BooleanField('avaliable', default=True)
    description = models.TextField('description', max_length=250, null=False)
    image = models.CharField('image', max_length=250, null=True)
