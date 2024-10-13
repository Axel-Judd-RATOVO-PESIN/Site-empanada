# Create your views here.
from django.shortcuts import render
from empanadas.models import Empanada
from empanadas.models import Ingredient
from empanadas.models import Composition

def empanadas(request):
    lesEmpanadas = Empanada.objects.all()
    return render(request,'empanadas/empanadas.html',{'empanadas' : lesEmpanadas} )

def ingredients(request):
    lesIngredients = Ingredient.objects.all()
    return render(request, 'empanadas/ingredients.html',{'ingredients' : lesIngredients} )

def empanada(request, empanada_id) :
	laEmpanada = Empanada.objects.get( idEmpanada= empanada_id)
	compositions = Composition.objects.filter(empanada = empanada_id)

	ingredients_list = []
	for compo in compositions:
		ingredients_list.append({
			'Ingredient' : compo.ingredient.nomIngredient,
			'Quantité' : compo.quantite
		})
	
	context = {
		'empanada': laEmpanada,
		'ingredients_list': ingredients_list,
	}	

	return render( request, 'empanadas/empanada.html', context )
