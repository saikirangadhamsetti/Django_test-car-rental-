from django.urls import path
from .views import AllVehicles,RentVehicle,userrentlog
urlpatterns=[
    path("",AllVehicles),
    path("rentavehicle/",RentVehicle),
    path("",userrentlog)
]