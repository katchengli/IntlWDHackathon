from django.db import models
from django.forms import ModelForm, Form

class Unit(models.Model):
    unit=models.CharField(max_length=200, default='Meters')
    def __str__(self): 
        return self.unit
        
class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['unit']