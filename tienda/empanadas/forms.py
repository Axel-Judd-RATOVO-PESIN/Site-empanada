from django.forms     import ModelForm
from empanadas.models import Ingredient

class IngredientForm(ModelForm):
	class Meta:
		model = Ingredient
		fields = ['nomIngredient']


#-------- VERSION NON-AUTOMATIQUE --------#

# from django import forms
# class IngredientForm(forms.Form):
#	nomIngredient = forms.CharField( label = 'nom ingrédient',
#					 max_length=50)
#

