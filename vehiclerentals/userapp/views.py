from django.shortcuts import render
from backapp.models import Vehicles,Rentlog
from .serializers import uservehicleserializer,userrentrequestserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
import json
# Create your views here.
@login_required
@api_view(["GET"])
def AllVehicles(request):
    m=Vehicles.objects.values_list().all()
    k=uservehicleserializer(m,many=True)
    return Response(k)


@login_required    
@api_view(["POST"])
def RentVehicle(request):
    m=userrentrequestserializer(data=request.data)
    if m.is_valid():
        m.save()
        return Response(m.data)
    else:
        return Response(m.errors)

@login_required
@api_view(["GET"])
def userrentlog(request):
    m=Rentlog.objects.all().filter(userid=id)
    #here id of active user can be retreived by using any authentication methods based on tokeninzing,jwt