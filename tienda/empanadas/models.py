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



class Empanda(models.Model) :
    #cle primaire, avec auto-increment
    idEmpanada    = models.AutoField(    primary_key    = True )
    #chaine de caractere de taille bornee
    nomEmpanada   = models.CharField(   max_length      = 50   )
    #nombre decimal, max 6 chiffres dont 2 apres la virgule
    prix          = models.DecimalField( max_digits     = 6, decimal_places = 2 )
    #version pytho, du toString(), utilise par django dans ses interfaces 
    def __str__(self) :
        return 'empanda'+self.nomEmpanada+' (prix:'+str(self.prix)+'€)'

