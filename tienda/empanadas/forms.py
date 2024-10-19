from django.forms     import ModelForm
from django	      import forms
from empanadas.models import Ingredient
from empanadas.models import Empanada
from empanadas.models import Composition

class IngredientForm(ModelForm):
	class Meta:
		model = Ingredient
		fields = ['nomIngredient']

class EmpanadaForm(ModelForm):
	class Meta:
		model = Empanada
		fields = ['nomEmpanada', 'prix']

class CompositionForm(ModelForm):
    class Meta:
        model = Composition  # Remplacez par le nom de votre modèle de composition
        fields = ['ingredient', 'quantite']  # Champs à inclure dans le formulaire

    # Définir les choix pour le champ ingredient
    ingredient = forms.ModelChoiceField(
        queryset=Ingredient.objects.all(),
        empty_label="Sélectionnez un ingrédient",  # Optionnel : message par défaut
        required=True  # Rendre le champ obligatoire
    )
    
    # Définir le champ quantite
    quantite = forms.CharField(
        max_length=100,  # Ajustez la longueur maximale selon vos besoins
        required=True,   # Rendre le champ obligatoire
        widget=forms.TextInput(attrs={'placeholder': 'Entrez la quantité'})  # Ajoute un placeholder
    )


#-------- VERSION NON-AUTOMATIQUE --------#

# from django import forms
# class IngredientForm(forms.Form):
#	nomIngredient = forms.CharField( label = 'nom ingrédient',
#					 max_length=50)
#

