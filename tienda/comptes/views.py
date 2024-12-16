from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from comptes.models import TiendaUser
from comptes.forms import TiendaUserForm
# Create your views here.


def connexion(request):
    usr = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username=usr, password=pwd)
    if user is None:
        return redirect('/login')
    else:
        login(request, user)
        return redirect('/empanadas')

def deconnexion(request):
    logout(request)
    return render(request, 'comptes/logout.html')

def formulaireProfil(request):
    user=None
    if request.user.is_authenticated:
        return render(request, 'comptes/profil.html', {'user' : TiendaUser.objects.get(id=request.user.id),})
    else:
        return redirect('/login')

def traitementFormulaireProfil(request):
    user=None

    if request.user.is_authenticated:
        user = TiendaUser.objects.get(id=request.user.id) #-- Recuperation de TiendaUser
        form = TiendaUserForm(request.POST, request.FILES, instance=user) #-- Recuperation du formulaire (qui est une instance de TiendaUser)

        if form.is_valid():
            form.save() #-- Sauvegarde de TiendaUser
            return redirect('/empanadas') #-- Redirection vers la page d'acceuil
    else:
        return redirect('/login')


def formulaireInscription(request):
    return render(request, 'comptes/formulaireInscription.html')

def traitementFormulaireInscription(request):
    user = TiendaUser()
    user.first_name = request.POST [ 'first_name' ]
    user.last_name = request.POST [ 'last_name' ]
    user.username = request.POST [ 'username' ]
    user.email = request.POST [ 'email' ]
    user.set_password(request.POST [ 'password' ])
    user.image = request.FILES [ 'image' ]
    user.save()
    login(request, user)
    return redirect('/empanadas')
