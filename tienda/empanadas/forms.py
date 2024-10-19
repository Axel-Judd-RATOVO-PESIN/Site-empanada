from django.forms     import ModelForm
from empanadas.models import Ingredient
from empanadas.models import Empanada

class IngredientForm(ModelForm):
	class Meta:
		model = Ingredient
		fields = ['nomIngredient']

class EmpanadaForm(ModelForm):
	class Meta:
		model = Empanada
		fields = ['nomEmpanada', 'prix']
		

#-------- VERSION NON-AUTOMATIQUE --------#

# from django import forms
# class IngredientForm(forms.Form):
#	nomIngredient = forms.CharField( label = 'nom ingrédient',
#					 max_length=50)
#

