from django.contrib import admin
from api.models import User, Categories, Cars, CarBookingDate

# Register your models here.

admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Cars)
admin.site.register(CarBookingDate)
