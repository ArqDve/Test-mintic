from django.shortcuts import render
from rest_framework import generics
from .serializers import PersonaSoporteSerializers
from .models import PersonaSoporte
from .serializers import PQRSerializer
from .models import PQR


class PersonaSoporteListCreate(generics.ListCreateAPIView):
    #PersonaSoporte.objects.all se hacen los filtros heredados de la clase. En este caso se recibe todo por.all  ORM
    queryset = PersonaSoporte.objects.all()
    serializer_class = PersonaSoporteSerializers

class PersonaSoporteUpdateDelete(generics.ListCreateAPIView):
    queryset = PersonaSoporte.objects.all()
    serializer_class = PersonaSoporteSerializers


class PQRSerializerListCreate(generics.ListCreateAPIView):
    #PersonaSoporte.objects.all se hacen los filtros heredados de la clase. En este caso se recibe todo por.all  ORM
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer

class PQRUpdateDelete(generics.ListCreateAPIView):
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer