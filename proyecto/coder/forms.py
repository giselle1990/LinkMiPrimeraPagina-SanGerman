from django import forms 

from . import models 

class deudorform(forms.ModelForm):
    class Meta:
        model= models.Deudor
        fields= "__all__"
        
class ClienteNuevoForm(forms.ModelForm):
    class Meta:
        model = models.ClienteNuevo
        fields = ['nombre', 'email', 'telefono']