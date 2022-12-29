from django.shortcuts import render
from backapp.models import Vehicles,Rentrequest,Rentlog,User
from .serializers import VehicleOwnerSerializer,Ownerrentapprovalserializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND,HTTP_200_OK
from rest_framework.response import Response
from django.contrib.auth.decorators import permission_required,login_required
@permission_required
@login_required
@api_view(["GET"])
def OwnerVehicleList(request,ownerid):
    m=Vehicles.objects.all().filter(OwnerId=ownerid)
    k=VehicleOwnerSerializer(m,many=True)
    return Response(k.data)
class VehicleCreate(APIView):
    def post(self,request):
        serialize=VehicleOwnerSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
@permission_required
@login_required
class ownervehicles(APIView):
    def put(self,request,ownerid,vehicleid):
        try:
            k=Vehicles.objects.all().get(id=vehicleid)&Vehicles.objects.all().get(OwnerId=ownerid)
        except:
            return Response({"Vehicle or Owner doesn't exist"},status=HTTP_404_NOT_FOUND)
        k=VehicleOwnerSerializer(Vehicles,data=request.data)
        if k.is_valid():
            k.save()
            return Response(k.data)
        return Response(k.errors)
    def delete(self,request,ownerid,vehicleid):
        try:
            k=Vehicles.objects.all().get(id=vehicleid)&Vehicles.objects.all().get(OwnerId=ownerid)
        except:
            return Response({"error:Vehicle or owner doesn't exist"},status=HTTP_404_NOT_FOUND)
        k.delete()
        return Response("Vehicle WAS DELETED")
@permission_required
@login_required
class Rentrequests(APIView):
    def get(self,request,ownerid):
        try:
            k=Rentrequest.objects.values().filter(ownerid=ownerid)
        except:
            return Response({"You have no rental requests"},status=HTTP_404_NOT_FOUND)
        r=Ownerrentapprovalserializer(k,many=True)
        return Response(r.data)
    def put(self,request,ownerid):
        try:
            k=Rentrequest.objects.all().filter(ownerid=ownerid) and Rentrequest.objects.all().filter(status='')
        except:
            return Response({"You have no rental requests"},status=HTTP_404_NOT_FOUND)
        k=Rentrequest(id=request.data.get("id"),ownerid=request.data.get("ownerid"),Vehicleid=request.data.get("Vehicleid"),pickupdatetime=request.data.get("pickupdatetime"),drop_offdatetime=request.data.get("drop_offdatetime"),status=request.data.get("status"),userid=request.data.get("userid"))
        k.save()
        h=User.objects.values_list("username").filter(id=ownerid)
        u=User.objects.values_list("username").filter(id=request.data.get("userid"))
        if(request.data.get("status")=="Accepted"):
            Rentlog(ownerid=request.data.get("ownerid"), Vehicleid=request.data.get("Vehicleid"),owner_username=h[0]["username"],customer_username=u[0]["username"])
        return Response("Data Added")
