from django.db import models
class Vehicles(models.Model):
    CarName=models.CharField(max_length=20)
    Seats=models.IntegerField()
    Large_bag=models.IntegerField()
    Small_bag=models.IntegerField()
    Mileage=models.CharField(max_length=20)
    Price_For_3Days=models.IntegerField()
    OwnerId=models.IntegerField()
    def __str__(self):
        return self.CarName
class User(models.Model):
    kk=(("customer","customer"),
        ("owner","owner"))
    UserName=models.CharField(max_length=20),
    Password=models.CharField(max_length=20),
    UserType=models.CharField(max_length=10,choices=kk),
class Rentlog(models.Model):
    ownerid=models.IntegerField()
    owner_username=models.CharField(max_length=10)
    customer_username=models.CharField(max_length=10)
    userid=models.IntegerField(default=0)
    Vehicleid=models.IntegerField()
class Rentrequest(models.Model):
    status=(('Accept','Accepted'),
    ('Reject','Rejected'))
    ownerid=models.IntegerField()
    Vehicleid=models.IntegerField()
    pickupdatetime=models.DateTimeField()
    drop_offdatetime=models.DateTimeField()
    status=models.CharField(max_length=10,choices=status,blank=True)