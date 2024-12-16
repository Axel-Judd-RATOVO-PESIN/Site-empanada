from django.forms import ModelForm
from comptes.models import TiendaUser

class TiendaUserForm(ModelForm): #--- TP3 Exo3 Question3 : creation d' un formulaire pour un User
    class Meta:
        model = TiendaUser
        fields = ['username','first_name','last_name','email','image']