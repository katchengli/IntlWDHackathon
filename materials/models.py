from django.db import models

class Material(models.Model):
	name=models.CharField(max_length=200)
	date_entered=models.DateTimeField('Date Entered')
	unit=models.ForeignKey('Unit')
	category = models.ForeignKey('Category')
	price=models.DecimalField(max_digits=6, decimal_places=2)
	quantity=models.DecimalField(max_digits=6, decimal_places=2)
    
class Unit(models.Model):
	unit=models.CharField(max_length=200)

class Category(models.Model):
	category=models.CharField(max_length=200)
	