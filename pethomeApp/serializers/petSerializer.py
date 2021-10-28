from pethomeApp.models.pet import Pet
from rest_framework import serializers


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id_pet', 'name', 'specie', 'breed', 'gender', 'bday_aprox',
                  'date_register', 'description', 'image', 'avaliable', 'user']
