"""
URL configuration for tienda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from empanadas import views

urlpatterns = [
    path('admin/', 					admin.site.urls),
    path('empanadas/', 					views.empanadas, name='liste_empanadas'),
    path('ingredients/', 				views.ingredients, name='liste_ingredients'),
    path('empanada/<int:empanada_id>',  		views.empanada, name='detailsEmpanada'),
    path('ingredients/add', 				views.formulaireCreationIngredient),
    path('ingredients/create',				views.creerIngredient, name='creerIngredient'),
    path('empanadas/add',               		views.formulaireCreationEmpanada),
    path('empanadas/create',				views.creerEmpanada, name='creerEmpanada'),
    path('empanada/<int:empanada_id>/addIngredient',	views.ajouterIngredientDsEmpanada),
    path('empanada/<int:empanada_id>/delete/',		views.supprimerEmpanada),
    path('empanada/<int:empanada_id>/update/',		views.afficherFormulaireModificationEmpanada),
    path('empanada/<int:empanada_id>/updated',		views.modifierEmpanada, name='editEmpanada'),
    path('ingredient/<int:ingredient_id>/delete/',	views.supprimerIngredient, name='supprimerIngredient'),
    path('ingredient/<int:ingredient_id>/update/',	views.afficherFromulaireModificationIngredient, name='afficherFormIngredient'),
    path('ingredient/<int:ingredient_id>/updated',      views.modifierIngredient, name='editIngredient'),
    path('empanadas/<int:empanada_id>/deleteIngredient/<int:ligne_id>/',  views.supprimerIngredientDansEmpanada),
]
