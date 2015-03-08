from django.db import models
from django import forms

class Material(models.Model):
	name=models.CharField(max_length=200)
	date_entered=models.DateTimeField('Date Entered', auto_now_add=True)
	unit=models.ForeignKey('Unit')
	#category = models.ForeignKey('Category')
	price=models.DecimalField(max_digits=6, decimal_places=2)
	quantity=models.DecimalField(max_digits=6, decimal_places=2)
	
	def __str__(self): 
		return self.name

class Unit(models.Model):
	unit=models.CharField(max_length=200)
	
	def __str__(self): 
		return self.unit

class Category(models.Model):
	category=models.CharField(max_length=200, default='No Category')
	
	def __str__(self): 
		return self.category

class UnitForm(forms.Form):
	unit = forms.CharField(label='Unit name', max_length=200)
	
	def __str__(self): 
		return self.unit