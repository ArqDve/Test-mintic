from rest_framework import serializers
from .models import PQR, PersonaSoporte

class PersonaSoporteSerializers(serializers.ModelSerializer):
    class Meta:
        model = PersonaSoporte
        fields = '__all__'

class PQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PQR
        fields = ['persona_soporte', 'estado', 'comentario']