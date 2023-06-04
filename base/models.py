from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
    

class Header(models.Model):
    header = models.CharField(max_length=50)
    header_text = models.TextField()
    picture = models.ImageField(upload_to='picture/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.header
class Signupbanner(models.Model):
    big_text = models.CharField(max_length=1000)
    small_text = models.TextField()
    signuppicture = models.ImageField(upload_to='signupbannerpicture/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.big_text
class SouthAfricaupdate(models.Model):
    big_text = models.CharField(max_length=100)
    small_text = models.TextField()
    southAfricaupdate = models.ImageField(upload_to='southafricaupdatepicture/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.big_text
    
class TrackingNumber(models.Model):
    Tracking_number = models.TextField(max_length=100)

    def __str__(self) -> str:
        return self.Tracking_number
    


class ShipmentDetails(models.Model):
    receiver_name = models.CharField(max_length=50)
    types_of_shipment = models.CharField(max_length=50)
    weight = models.CharField(max_length=7)
    packages = models.CharField(max_length=3)
    product = models.CharField(max_length=3)
    payment_mode = models.CharField(max_length=20)
    current_location = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=20)
    destination = models.CharField(max_length=100)
    pickup_time = models.CharField(max_length=20)
    courier = models.CharField(max_length=50)
    tracking_number = models.CharField(max_length=100)
    origin = models.CharField(max_length=50)
    pickup_date = models.CharField(max_length=20)
    expected_delivery_date = models.CharField(max_length=20)
    comment = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    
    def __str__(self) -> str:
        return self.receiver_name
    

class ShipperDetails(models.Model):
    shipmentDetails = models.ForeignKey(ShipmentDetails, on_delete=models.CASCADE)
    shipper_name =  models.CharField(max_length=50)
    phone_number =  models.CharField(max_length=20)
    address =  models.CharField(max_length=100)
    email = models.CharField(max_length=100)



class receiverDetails(models.Model):
    shipmentDetails = models.ForeignKey(ShipmentDetails, on_delete=models.CASCADE)
    receiver_name =  models.CharField(max_length=50)
    phone_number =  models.CharField(max_length=20)
    address =  models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class BannerPictures(models.Model):
    name = models.CharField(max_length=20)
    bannerpictures1 = models.ImageField(upload_to='bannerpictures/')
    bannerpictures2 = models.ImageField(upload_to='bannerpictures/')
    bannerpictures3 = models.ImageField(upload_to='bannerpictures/')
    updated = models.DateTimeField(auto_now=True)



    def __str__(self) -> str:
        return self.name
