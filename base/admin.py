from django.contrib import admin
from .models import UserProfile, Header,Signupbanner,SouthAfricaupdate, TrackingNumber, ShipmentDetails, ShipperDetails, receiverDetails,BannerPictures

admin.site.register(UserProfile)
admin.site.register(Header)
admin.site.register(Signupbanner)
admin.site.register(SouthAfricaupdate)
admin.site.register(TrackingNumber)
admin.site.register(BannerPictures)

class ShipperDetailsInline(admin.TabularInline):
    model = ShipperDetails
    extra = 1

class receiverDetailsInline(admin.TabularInline):
    model = receiverDetails
    extra = 1

@admin.register(ShipmentDetails)
class ShipmentDetailsadmin(admin.ModelAdmin):
    inlines = [
        ShipperDetailsInline,
        receiverDetailsInline,
    ]
