from django.db import models
from farmersdt .models import Farmers

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    

class ProductType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='product_category')
    product_type = models.ForeignKey(ProductType,on_delete=models.CASCADE,related_name='product_producttype')
    
    def __str__(self):
        return self.name


class Plant(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='plant_category')
    products = models.ManyToManyField(Product,blank=True,related_name='plant_products')
    
    def __str__(self):
        return self.name
    

class CropsinFarmer(models.Model):
    farmer = models.ForeignKey(Farmers,on_delete=models.CASCADE,related_name='cropsinfarmer_farmer')
    plant = models.ForeignKey(Plant,on_delete=models.CASCADE,related_name='cropsinfarmer_plant')
    
    def __str__(self):
        return self.farmer
    

class ProductStock(models.Model):
    crops_in_farmer = models.ForeignKey(CropsinFarmer,on_delete=models.CASCADE,related_name='productstock_cropsinfarmer')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='productstock_product')
    quantity = models.FloatField()
    
    def __str__(self):
        return self.crops_in_farmer