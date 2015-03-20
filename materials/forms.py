from django.forms import Form, ModelForm
from materials.models import Material
from management.models import Unit

class MaterialForm(ModelForm):
    class Meta:
        model = Material
        #widgets = {
            # 'name': forms.TextInput(attrs={'class': 'form-control'}), 
            # 'unit', 'price', 'quantity'
        # }
        fields = ['name', 'unit', 'price', 'quantity']