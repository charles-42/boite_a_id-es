from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


from .models import Idee

def hello(request):

    return HttpResponse(f"""
        <h1>Hello Django from container!</h1>
""")


def accueil(request):

    idees = Idee.objects.all()

    return render(request, 'main/accueil.html',{'liste_idee': idees})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Si le formulaire est valide on crée l'utilisateur
            form.save()
            # Et ensuite on le log
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        
    else:
        form = UserCreationForm()

    return render(request, 'main/signup.html', {'form': form})


from django.contrib.auth.forms import  AuthenticationForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

    else:
        form = AuthenticationForm()

    return render(request, 'main/signup.html', {'form': form})