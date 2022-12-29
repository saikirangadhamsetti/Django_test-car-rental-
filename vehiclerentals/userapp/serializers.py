from rest_framework import serializers
from backapp.models import Vehicles,Rentrequest
class uservehicleserializer(serializers.ModelSerializer):
    model=Vehicles
    fields="__all__"
class userrentrequestserializer(serializers.ModelSerializer):
    model=Rentrequest
    fields=["ownerid","Vehicleid","pickupdatetime","dropoffdatetime"]


    