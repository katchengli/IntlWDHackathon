from django.shortcuts import render
from materials.models import Material, Unit

# class UnitForm(ModelForm):
	# class Meta:
	# model = Unit
	# fields = ['name']

def index(request):
	unit = Unit.objects.all()
	return render(request, 'materials/index.html', {'unit': unit})

	