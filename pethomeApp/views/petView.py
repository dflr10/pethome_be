from rest_framework import status, views
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage

from pethomeApp.models import Pet
from pethomeApp.serializers import PetSerializer

# Create your views here.


@csrf_exempt
def petAPI(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            pets = Pet.objects.all()
            serializer = PetSerializer(pets, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            pet = Pet.objects.get(id_pet=pk)
            serializer = PetSerializer(pet)
            return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added successfuly", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        pet = Pet.objects.get(id_pet=data['id_pet'])
        serializer = PetSerializer(pet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Update successfuly", safe=False)
        return JsonResponse("Failed to update")
    elif request.method == 'DELETE':
        pet = Pet.objects.get(id_pet=pk)
        pet.delete()
        return JsonResponse("Deleted successfuly", safe=False)


@csrf_exempt
def saveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
