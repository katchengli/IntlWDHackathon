from django.shortcuts import render
from django.shortcuts import render
from materials.models import Material

#def materials(request):
	#return render(request, 'materials/materials.html', {'materials': materials})


def index(request):
	materials = Material.objects.order_by('name')
	return render(request, 'materials/index.html', {'materials': materials})


	