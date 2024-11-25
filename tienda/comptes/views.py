from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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
