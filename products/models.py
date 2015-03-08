from django.db import models
from django import forms

class Product(models.Model):
    name=models.CharField(max_length=200)
    date_entered=models.DateTimeField('Date Entered', auto_now_add=True)
    description=models.CharField(max_length=800)
    total=models.DecimalField(max_digits=6, decimal_places=2)
    materials = models.ManyToManyField('materials.Material')
	
    def __str__(self): 
        return self.name