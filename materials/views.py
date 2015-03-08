from django.shortcuts import render
from materials.models import Material, Unit, UnitForm
from django.http import HttpResponseRedirect

# class UnitForm(ModelForm):
	# class Meta:
	# model = Unit
	# fields = ['name']

def index(request):
	unit = Unit.objects.all()
	material = Material.objects.all()
    
	print("@@@@@@@@@@@@@@@@@@@@@@@@")
	for m in material:
		print(m)
    
	return render(request, 'materials/index.html', {'materials': material, 'units': unit})
	#return render(request, 'materials/index.html', {'unit': unit})

def new(request):
# if this is a POST request we need to process the form data
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = UnitForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
		# process the data in form.cleaned_data as required
		# ...
		# redirect to a new URL:
			return HttpResponseRedirect('/materials/')
			# if a GET (or any other method) we'll create a blank form
	else:
		form = UnitForm()
	return render(request, 'materials/new.html', {'form': form})