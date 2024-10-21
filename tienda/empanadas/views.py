# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from empanadas.models import Empanada
from empanadas.models import Ingredient
from empanadas.models import Composition
from empanadas.forms  import IngredientForm
from empanadas.forms  import EmpanadaForm
from empanadas.forms  import CompositionForm
from django.http import HttpResponse #--- Importation de la librairie http pour afficher des messages
from django.contrib import messages #--- Optionnel, mais me permet d'afficher un message suite à une action


def empanadas(request):
    lesEmpanadas = Empanada.objects.all()
    return render(request,'empanadas/empanadas.html',{'empanadas' : lesEmpanadas} )

def ingredients(request):
    lesIngredients = Ingredient.objects.all()
    return render(request, 'empanadas/ingredients.html',{'ingredients' : lesIngredients} )

def empanada(request, empanada_id) :
	laEmpanada = Empanada.objects.get( idEmpanada= empanada_id)
	compositions = Composition.objects.filter(empanada = empanada_id)
	allIngredients = Ingredient.objects.all() #-- Recup tous les ingredient de la BD

	ingredients_list = []
	for compo in compositions:
		ingredients_list.append({
			'idIngredient' : compo.ingredient.idIngredient,
			'Ingredient' : compo.ingredient.nomIngredient,
			'Quantite' : compo.quantite
		})
	
	context = {
		'empanada': laEmpanada,
		'ingredients_list': ingredients_list,
		'allIngredients' : allIngredients
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
	form =  EmpanadaForm(request.POST)
	if form.is_valid():
		nomEmp = form.cleaned_data['nomEmpanada']
		prixEmp = form.cleaned_data['prix']
		emp = Empanada()
		emp.nomEmpanada = nomEmp
		emp.prix = prixEmp
		emp.save()
		return render(request, 'empanadas/traitementFormulaireCreationEmpanada.html', {'nomEmp' : nomEmp ,'prixEmp' : prixEmp}, )	
	else:
		return render(request, 'empanadas/formulaireCreationEmpanada.html', {'erreurs' : form.errors}, )


def ajouterIngredientDsEmpanada(request, empanada_id):
	form = CompositionForm(request.POST)
	if form.is_valid():
		ingr = form.cleaned_data['ingredient']
		qt = form.cleaned_data['quantite']

		if not qt.endswith('g'): #-- Nous permet d'ajouter l'unité de mesure pour la quantite
			qt += 'g'

		emp = Empanada.objects.get(idEmpanada=empanada_id)
		recherche = Composition.objects.filter(empanada=empanada_id, ingredient=ingr.idIngredient)
		if recherche.count() > 0:
			ligne = recherche.first()
		else:
			ligne = Composition()
			ligne.ingredient = ingr
			ligne.empanada = emp
		ligne.quantite = qt
		ligne.save()
		return redirect('/empanada/%d'% empanada_id)
	else:
		return render(request, 'empanadas/formulaireNonValide.html', {'erreur' : form.errors})


def supprimerEmpanada(request, empanada_id):
	emp = Empanada.objects.get( idEmpanada= empanada_id) #--- On recup la empanada à supprimer
	emp.delete()
	return redirect('liste_empanadas') #-- 'liste_empanadas' est le nom donné à l'url 'empanadas/'


def afficherFormulaireModificationEmpanada(request, empanada_id):
	emp = Empanada.objects.get( idEmpanada= empanada_id)
	return render( request, 'empanadas/formulaireModificationEmpanada.html', {'empanada': emp} )


def modifierEmpanada(request, empanada_id):
	empToEdit = Empanada.objects.get( idEmpanada= empanada_id)
	form = EmpanadaForm(request.POST, instance=empToEdit) #-- Recup formulaire posté avec pour instance la empanada récupérée
	if form.is_valid():
		form.save()
		return redirect('liste_empanadas')
	else:
		return render(request, 'empanadas/formulaireNonValide.html', {'erreur' : form.errors})
