from django.urls import path
from .views import OwnerVehicleList,ownervehicles,VehicleCreate,Rentrequests
urlpatterns=[

path("vehicleslist/",OwnerVehicleList),
path("vehicle/<int:vehicleid>",ownervehicles.as_view()),
path("",VehicleCreate.as_view()),
path("rentrequests/",Rentrequests.as_view())
]