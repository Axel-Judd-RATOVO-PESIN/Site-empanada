from django.db import models

# Create your models here.

class Ingredient(models.Model) :
    #cle primaire, avec auto-increment
    idIngredient = models.AutoField( primary_key = True )
    #chaine de caractere de taille bornee
    nomIngredient = models.CharField( max_length = 50 )
    #version python du toString(), utilise par django dans ses interfaces
    def __str__(self) :
        return self.nomIngredient



class Empanada(models.Model) :
    #cle primaire, avec auto-increment
    idEmpanada    = models.AutoField(    primary_key    = True )
    #chaine de caractere de taille bornee
    nomEmpanada   = models.CharField(   max_length      = 50   )
    #nombre decimal, max 6 chiffres dont 2 apres la virgule
    prix          = models.DecimalField( max_digits     = 6, decimal_places = 2 )

    image = models.ImageField( default = 'imagesEmpanadas/default.png', upload_to = 'imagesEmpanadas/')

    #version pytho, du toString(), utilise par django dans ses interfaces 
    def __str__(self) :
        return 'Empanda '+self.nomEmpanada+' (prix:'+str(self.prix)+'€)'

class Composition(models.Model):
    class Meta:
        unique_together = ('ingredient','empanada')
    idComposition = models.AutoField( primary_key = True )
    ingredient = models.ForeignKey( Ingredient, on_delete = models.CASCADE )
    empanada = models.ForeignKey( Empanada, on_delete = models.CASCADE )
    quantite = models.CharField( max_length = 100 )
    def __str__(self):
    	return f"Composition: {self.quantite}, Empanada ID: {self.empanada_id.id}, Ingredient ID: {self.ingredient_id.id}"
