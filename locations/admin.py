from django.contrib import admin
from .models import Countrty,State,District,Panchayats,RevenueVillage,LocalVillage
# Register your models here.

admin.site.register(Countrty)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Panchayats)
admin.site.register(RevenueVillage)
admin.site.register(LocalVillage)