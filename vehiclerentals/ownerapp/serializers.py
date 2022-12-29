from rest_framework import serializers
from backapp.models import Vehicles,Rentrequest
class VehicleOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicles
        fields="__all__"  
class Ownerrentapprovalserializer(serializers.ModelSerializer):
    class Meta:
        model=Rentrequest
        fields="__all__"