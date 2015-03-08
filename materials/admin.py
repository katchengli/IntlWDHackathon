from django.contrib import admin

# Register your models here.

from materials.models import Material, Category
from management.models import Unit, UnitForm

admin.site.register(Material)
admin.site.register(Unit)
admin.site.register(Category)
