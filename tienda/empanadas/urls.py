from django.urls import path
from empanadas import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('empanadas/',                                  views.empanadas, name='liste_empanadas'),
    path('ingredients/',                                views.ingredients, name='liste_ingredients'),
    path('empanada/<int:empanada_id>',                  views.empanada, name='detailsEmpanada'),
    path('ingredients/add',                             views.formulaireCreationIngredient),
    path('ingredients/create',                          views.creerIngredient, name='creerIngredient'),
    path('empanadas/add',                               views.formulaireCreationEmpanada),
    path('empanadas/create',                            views.creerEmpanada, name='creerEmpanada'),
    path('empanada/<int:empanada_id>/addIngredient',    views.ajouterIngredientDsEmpanada),
    path('empanada/<int:empanada_id>/delete/',          views.supprimerEmpanada),
    path('empanada/<int:empanada_id>/update/',          views.afficherFormulaireModificationEmpanada),
    path('empanada/<int:empanada_id>/updated',          views.modifierEmpanada, name='editEmpanada'),
    path('ingredient/<int:ingredient_id>/delete/',      views.supprimerIngredient, name='supprimerIngredient'),
    path('ingredient/<int:ingredient_id>/update/',      views.afficherFromulaireModificationIngredient, name='afficherFormIngredient'),
    path('ingredient/<int:ingredient_id>/updated',      views.modifierIngredient, name='editIngredient'),
    path('empanadas/<int:empanada_id>/deleteIngredient/<int:ligne_id>/',  views.supprimerIngredientDansEmpanada),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #-- AFIN DE NOUS PERMETTRE D'AFFICHER LES IMAGES DES EMP>

