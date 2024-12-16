# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from empanadas.models import Empanada, Ingredient, Composition
from empanadas.forms import IngredientForm, EmpanadaForm, CompositionForm
from django.http import HttpResponse #--- Importation de la librairie http pour afficher des messages
from django.contrib import messages #--- Optionnel, mais me permet d'afficher un message suite à une action
from django.contrib.auth.models import User #--- TP12

# Vérifie si l'utilisateur est un membre du staff
def is_staff(user):
    return user.is_staff


def empanadas(request):
    lesEmpanadas = Empanada.objects.all()
    return render(request,'empanadas/empanadas.html',{'empanadas' : lesEmpanadas} )


def ingredients(request):
	user = None
	if request.user.is_staff:
		lesIngredients = Ingredient.objects.all()
		user = User.objects.get(id=request.user.id)
		return render(request, 'empanadas/ingredients.html',{'ingredients' : lesIngredients, 'user' : user,} )
	elif request.user.is_authenticated:
		return redirect('/empanadas')
	else:
		return redirect('/login')

def empanada(request, empanada_id) :
	laEmpanada = Empanada.objects.get( idEmpanada= empanada_id)
	compositions = Composition.objects.filter(empanada = empanada_id)
	allIngredients = Ingredient.objects.all() #-- Recup tous les ingredient de la BD

	ingredients_list = []
	for compo in compositions:
		ingredients_list.append({
			'idIngredient' : compo.ingredient.idIngredient,
			'Ingredient' : compo.ingredient.nomIngredient,
			'Quantite' : compo.quantite,
			'idComposition' : compo.idComposition #-- Util pour la fonction supprimerIngredientDansEmpanada
		})
	
	context = {
		'empanada': laEmpanada,
		'ingredients_list': ingredients_list,
		'allIngredients' : allIngredients
	}	

	return render( request, 'empanadas/empanada.html', context )




#-------------------------------------- PARTIE : CREATION D'UN INGREDIENT ----------------------------------------------------------


def formulaireCreationIngredient(request):
	if request.user.is_staff:
		return render( request, 'empanadas/formulaireCreationIngredient.html' )
	else:
		return redirect('/empanadas')

def creerIngredient(request):
	if request.user.is_staff:
		form = IngredientForm(request.POST)
		if form.is_valid():
			nomIngr 		= form.cleaned_data['nomIngredient']
			ingr 			= Ingredient()
			ingr.nomIngredient 	= nomIngr
			ingr.save()
			return render(request, 'empanadas/traitementFormulaireCreationIngredient.html', {'nom' : nomIngr}, )
		else:
			return render(request, 'empanadas/formulaireNonValide.html', {'erreurs' : form.errors}, )
	else:
		return redirect('/empanadas')




#--------------------------------------- PARTIE : CREATION D'UNE EMPANADA ------------------------------------------------------

def formulaireCreationEmpanada(request):
    if request.user.is_staff:
        return render(request, 'empanadas/formulaireCreationEmpanada.html')
    else:
        return redirect('/empanadas')


def creerEmpanada(request):
    if request.user.is_staff:
        form = EmpanadaForm(request.POST, request.FILES)
        if form.is_valid():
            nomEmp = form.cleaned_data['nomEmpanada']
            prixEmp = form.cleaned_data['prix']
            emp = Empanada()
            emp.nomEmpanada = nomEmp
            emp.prix = prixEmp
            emp.image = request.FILES['image']
            emp.save()
            return render(request, 'empanadas/traitementFormulaireCreationEmpanada.html', {'nomEmp': nomEmp, 'prixEmp': prixEmp})
        else:
            return render(request, 'empanadas/formulaireCreationEmpanada.html', {'erreurs': form.errors})
    else:
        return redirect('/empanadas')




#------------------------------------------------ PARTIE : AJOUT D'UN INGREDIENT POUR UN EMPANADA ----------------------------------

def ajouterIngredientDsEmpanada(request, empanada_id):
    if request.user.is_staff:
        form = CompositionForm(request.POST)
        if form.is_valid():
            ingr = form.cleaned_data['ingredient']
            qt = form.cleaned_data['quantite']
            
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
            return redirect('detailsEmpanada', empanada_id)
        else:
            return render(request, 'empanadas/formulaireNonValide.html', {'erreur': form.errors})
    else:
        return redirect('/empanadas')




#-------------------------------------------- PARTIE : TRAITEMENT D'UNE EMPANADA ---------------------------------------------------

def supprimerEmpanada(request, empanada_id):
    if request.user.is_staff:
        emp = Empanada.objects.get(idEmpanada=empanada_id)
        emp.delete()
        return redirect('liste_empanadas')  # 'liste_empanadas' est le nom donné à l'URL 'empanadas/'
    else:
        return redirect('/empanadas')


def afficherFormulaireModificationEmpanada(request, empanada_id):
    if request.user.is_staff:
        emp = Empanada.objects.get(idEmpanada=empanada_id)
        return render(request, 'empanadas/formulaireModificationEmpanada.html', {'empanada': emp})
    else:
        return redirect('/empanadas')


def modifierEmpanada(request, empanada_id):
    if request.user.is_staff:
        empToEdit = Empanada.objects.get(idEmpanada=empanada_id)
        form = EmpanadaForm(request.POST, request.FILES, instance=empToEdit)
        if form.is_valid():
            if 'image' in request.FILES:
                empToEdit.image = request.FILES['image']
            empToEdit.save()
            return redirect('detailsEmpanada', empanada_id)
        else:
            return render(request, 'empanadas/formulaireNonValide.html', {'erreur': form.errors})
    else:
        return redirect('/empanadas')



#----------------------------------------------- PARTIE : TRAITEMENT D'UN INGREDIENT --------------------------------------------------

def supprimerIngredient(request, ingredient_id):
    if request.user.is_staff:
        ing = Ingredient.objects.get(idIngredient=ingredient_id)
        ing.delete()
        return redirect('liste_ingredients')
    else:
        return redirect('/empanadas')


def afficherFormulaireModificationIngredient(request, ingredient_id):
    if request.user.is_staff:
        ingr = Ingredient.objects.get(idIngredient=ingredient_id)
        return render(request, 'empanadas/formulaireModificationIngredient.html', {'ingredient': ingr})
    else:
        return redirect('/empanadas')

def modifierIngredient(request, ingredient_id):
    if request.user.is_staff:
        ingrToEdit = Ingredient.objects.get(idIngredient=ingredient_id)
        form = IngredientForm(request.POST, instance=ingrToEdit)
        if form.is_valid():
            form.save()
            return redirect('liste_ingredients')
        else:
            return render(request, 'empanadas/formulaireNonValide.html', {'erreur': form.errors})
    else:
        return redirect('/empanadas')




#------------------------------------------ PARTIE : SUPPRESSION D'UN INGREDIENT DANS UNE COMPOSITION D'UNE EMPANADA -------------------------------


def supprimerIngredientDansEmpanada(request, empanada_id, ligne_id):
    if request.user.is_staff:
        try:
            composition = Composition.objects.get(empanada=empanada_id, idComposition=ligne_id)
            composition.delete()
            messages.success(request, "L'ingrédient a bien été supprimé.")
        except Composition.DoesNotExist:
            messages.error(request, "Erreur : l'ingrédient à supprimer n'existe pas.")

        return redirect('detailsEmpanada', empanada_id=empanada_id)  # Redirection vers la page détails d'une empanada
    else:
        return redirect('/empanadas')

