from django.db import models

# Create your models here.

class FPO(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class AEO(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    fpo = models.ForeignKey(FPO,on_delete=models.CASCADE,related_name='aeo_fpo')
    
    def __str__(self):
        return self.name
    

class ICS(models.Model):
    name = models.CharField(max_length=100)
    register_date = models.DateField()
    fpo = models.ForeignKey(FPO,on_delete=models.CASCADE,related_name='ics_fpo')
    
    def __str__(self):
        return self.name
    
    

class VFC(models.Model):
    name = models.CharField(max_length=100)
    fpo = models.ForeignKey(FPO,on_delete=models.CASCADE,related_name='vfc_fpo')
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    panchayats = models.CharField(max_length=255)
    revenue_village = models.CharField(max_length=255)
    local_village = models.CharField(max_length=255)    
    ics = models.ManyToManyField(ICS,related_name='vfc_ics')
    aeo = models.ForeignKey(AEO,on_delete=models.CASCADE,related_name='vfc_aeo')
    
    def __str__(self):
        return self.name


class Farmers(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    panchayats = models.CharField(max_length=255)
    fpo = models.ForeignKey(FPO,on_delete=models.CASCADE,related_name='farmers_fpo')
    ics = models.ForeignKey(ICS,on_delete=models.CASCADE,related_name='farmers_ics')
    vfc = models.ForeignKey(VFC,on_delete=models.CASCADE,related_name='farmers_vfc')
    