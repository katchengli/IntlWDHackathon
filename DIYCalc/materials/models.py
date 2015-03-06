from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=200)
    date_entered = models.DateTimeField('Date Entered')
    unit = models.ForeignKey('Unit')
    
class Unit(models.Model):
    unit = models.CharField(max_length=200)
