from django.contrib import admin
from . models import Company, BusInfo, Seats, Passenger, Rating
# Register your models here.

admin.site.register(Company)
admin.site.register(BusInfo)
admin.site.register(Seats)
admin.site.register(Passenger)
admin.site.register(Rating)
