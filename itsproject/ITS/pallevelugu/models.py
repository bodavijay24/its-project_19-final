# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Members(models.Model):
    id=models.AutoField(primary_key=True)
    Hid=models.IntegerField()
    Name=models.CharField(max_length=250)
    Gender=models.CharField(max_length=10)
    Age=models.IntegerField()
    passwd=models.CharField(max_length=10,null=True)
    Members=models.IntegerField(null=True)
    Photos=models.ImageField(upload_to='media/', null=True)
    AadharNo=models.IntegerField(null=True,unique=True)
    Longitude=models.DecimalField(max_digits=20,decimal_places=10,null=True)
    Latitude=models.DecimalField(max_digits=20,decimal_places=10,null=True)
    Income=models.IntegerField(null=True)
    def __str__(self): 
       return ' '.join([str(self.id),str(self.Hid),str(self.Name),str(self.Gender),str(self.AadharNo),str(self.Age),str(self.Photos),str(self.Latitude),str(self.Longitude),str(self.Income)])
"""class Households(models.Model):
    id= models.AutoField(primary_key=True)
    Hid=models.ForeignKey(Members,on_delete=models.CASCADE,related_name='+',null=True)
    Longitude=models.DecimalField(max_digits=20,decimal_places=10)
    Latitude=models.DecimalField(max_digits=20,decimal_places=10)
    Income=models.IntegerField()
    def __str__(self): 
       return str(self.id)"""
    
class Farms(models.Model):
    F_id=models.AutoField(primary_key=True)
    H_id=models.ForeignKey(Members,on_delete=models.CASCADE,null=True)
    Area=models.FloatField()
    aLongitude=models.DecimalField(max_digits=20,decimal_places=10,null=True)
    aLatitude=models.DecimalField(max_digits=20,decimal_places=10,null=True)
    bLongitude=models.DecimalField(max_digits=20,decimal_places=10,null=True)
    bLatitude=models.DecimalField(max_digits=20,decimal_places=10,null=True)
    cLongitude=models.DecimalField(max_digits=20,decimal_places=10,null=True)
    cLatitude=models.DecimalField(max_digits=20,decimal_places=10,null=True)
    dLongitude=models.DecimalField(max_digits=20,decimal_places=10,null=True)
    dLatitude=models.DecimalField(max_digits=20,decimal_places=10,null=True)
    season=models.CharField(max_length=20,null=True)
    crop=models.CharField(max_length=20,null=True)
    def getHid(self):
        return self.Members.Hid
    def __str__(self):
	return ' '.join([str(self.F_id),str(self.H_id),str(self.Area),str(self.aLongitude),str(self.aLatitude),str(self.bLongitude),str(self.bLatitude),str(self.cLongitude),str(self.cLatitude),str(self.dLongitude),str(self.dLatitude),str(self.season),str(self.crop),])
    

class Crop(models.Model):
	M_id=models.AutoField(primary_key=True)
	F_id=models.ForeignKey(Farms,on_delete=models.CASCADE,related_name='+',null=True)
	season=models.CharField(max_length=20,null=True)
	crop=models.CharField(max_length=20,null=True)
	profit=models.IntegerField(null=True)
	def __str__(self):
		return ' '.join([str(self.M_id),str(self.F_id),str(self.season),str(self.crop)])
	
class Wells(models.Model):
    W_id=models.AutoField(primary_key=True)
    M_id=models.ForeignKey(Members,on_delete=models.CASCADE,related_name='+',null=True)
    Longitude=models.DecimalField(max_digits=20,decimal_places=10)
    Latitude=models.DecimalField(max_digits=20,decimal_places=10)
    Depth=models.IntegerField()
    AvgWaTyield=models.IntegerField(null=True)
    #Pic=models.ImageField(upload_to="images/",null=True)
    #Audio=models.FileField(upload_to = u'mp3/', max_length=200,null=True)
    
    def __str__(self):
	return ' '.join([str(self.W_id),str(self.Longitude),str(self.Latitude),str(self.Depth)])
class Vill(models.Model):
	D_id=models.AutoField(primary_key=True)
	Village=models.CharField(max_length=200,null=True)
	def __str__(self):
		return ' '.join([str(self.D_id),str(self.Village)])
class Medicare(models.Model):
	mid=models.AutoField(primary_key=True)
	Did=models.ForeignKey(Vill,on_delete=models.CASCADE,related_name='+',null=True)
	Disease=models.CharField(max_length=200,null=True)
	Vaccine=models.CharField(max_length=200,null=True)
	Choices=(('Yes','Yes'),('No','No'),)
	Hospital=models.CharField(max_length=5, choices=Choices)
	def __str__(self):
		return ' '.join([str(self.mid),str(self.Did),str(self.Disease),str(self.Vaccine),str(self.Hospital)])
class MediUpdates(models.Model):
		updates=models.CharField(max_length=2000000000000,null=True)
class Dealer(models.Model):
	H_id=models.ForeignKey(Members,on_delete=models.CASCADE,null=True)
	crop=models.ForeignKey(Crop,on_delete=models.CASCADE,related_name='+',null=True)
	Quantity=models.IntegerField(null=True)
	MarketPrice=models.IntegerField(null=True)
	def __str__(self):
		return ' '.join([str(self.H_id),str(self.crop),str(self.Quantity),str(self.MarketPrice)])
	
	
   

