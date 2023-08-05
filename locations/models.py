from django.db import models


# Create your models here.

class Countrty(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name



class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Countrty,on_delete=models.CASCADE,related_name='state_country')
    
    def __str__(self):
        return self.name
    


class District(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State,on_delete=models.CASCADE,related_name='district_state')
    
    def __str__(self):
        return self.name



class Panchayats(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District,on_delete=models.CASCADE,related_name='panchayats_districts')
    panchayat_code = models.IntegerField()
    fpo = models.ForeignKey('farmersdt.FPO',on_delete=models.CASCADE,related_name='panchayat_fpo')
    
    def __str__(self):
        return self.name



class RevenueVillage(models.Model):
    name = models.CharField(max_length=100)
    panchayats = models.ForeignKey(Panchayats,on_delete=models.CASCADE,related_name='revenuevillage_panchayats',default=1)
    
    def __str__(self):
        return self.name



class LocalVillage(models.Model):
    name = models.CharField(max_length=100)
    revenue_village = models.ForeignKey(RevenueVillage, on_delete=models.CASCADE, related_name='localvillage_revenuevillage',default=1)

    def __str__(self):
        return self.name



class PostOffice(models.Model):
    name = models.CharField(max_length=100)
    local_village = models.ForeignKey(LocalVillage,on_delete=models.CASCADE,related_name='postoffice_localvillage',default=1)
    
    def __str__(self):
        return self.name

    
    
