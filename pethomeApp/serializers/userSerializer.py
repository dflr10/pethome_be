from rest_framework import serializers
from pethomeApp.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id_user', 'username', 'password', 'name', 'email']


def create(self, validated_data):
    userInstance = User.objects.create(**validated_data)
    return userInstance


def to_representation(self, obj):
    user = User.objects.get(id_user=obj.id_user)
    return {
        'id_user': user.id_user,
        'username': user.username,
        'name': user.name,
        'email': user.email,
    }
