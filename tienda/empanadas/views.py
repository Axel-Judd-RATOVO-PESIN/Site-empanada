# Create your views here.
from django.shortcuts import render
from empanadas.models import Empanada
from empanadas.models import Ingredient
from empanadas.models import Composition
from empanadas.forms  import IngredientForm

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
			'Quantite' : compo.quantite
		})
	
	context = {
		'empanada': laEmpanada,
		'ingredients_list': ingredients_list,
	}	

	return render( request, 'empanadas/empanada.html', context )


def formulaireCreationIngredient(request):
	return render( request, 'empanadas/formulaireCreationIngredient.html' )

def creerIngredient(request):
	form = IngredientForm(request.POST)
	if form.is_valid():
		nomIngr 		= form.cleaned_data['nomIngredient']
		ingr 			= Ingredient()
		ingr.nomIngredient 	= nomIngr
		ingr.save()
		return render(request, 'empanadas/traitementFormulaireCreationIngredient.html', {'nom' : nomIngr}, )
	else:
		return render(request, 'empanadas/formulaireNonValide.html', {'erreurs' : form.errors}, )

def formulaireCreationEmpanada(request):
	return render( request, 'empanadas/formulaireCreationEmpanada.html')

def creerEmpanada(request):
	form = EmpanadaForm(request.POST)
	if form.is_valid():
		nomEmp = form.cleaned_data['nomEmpanada']
		prixEmp = form.cleand_data['prix']
		emp = Empanada()
		emp.nomEmpanada = nomEmp
		emp.prix = prixEmp
		emp.save()
		return render(request, 'empanadas/traitementFormulaireCreationEmpanada.html', {'nomEmp' : nomEmp ,'prixEmp' : prixEmp}, )
	else:
		return render(request, 'empanadas/formulaireNonValide.html', {'erreurs' : form.errors}, )


