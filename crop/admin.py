from django.contrib import admin
from .models import Category,ProductType,Product,Plant,CropsinFarmer,ProductStock

# Register your models here.
admin.site.register(Category)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Plant)
admin.site.register(CropsinFarmer)
admin.site.register(ProductStock)
