from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from django.contrib.auth import login, logout
from .models import PracovniPozice
from .forms import PracovniPoziceFormular

#Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage') 
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect(reverse('homepage'))

def index(request):
    pracovni_pozice = PracovniPozice.objects.all()
    vysledek_hledani = request.GET.get('search', '')
    if vysledek_hledani:
        pracovni_pozice = PracovniPozice.objects.filter(nazev__icontains=vysledek_hledani)
    else:
        pracovni_pozice = PracovniPozice.objects.all()
    return render(request, 'index.html', {'pracovni_pozice': pracovni_pozice})


def detail_pozice(request, slug):
    pozice =  get_object_or_404(PracovniPozice, slug=slug)
    return render(request, 'detail_pozice.html', {'pozice': pozice})


def vytvorit_pracovni_pozici(request):
    if request.method == 'POST':
        form = PracovniPoziceFormular(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = PracovniPoziceFormular()
    return render(request, 'vytvorit_pracovni_pozici.html', {'form': form})


def succeses_page_form(request):
    return render(request , 'succeses_page_form.html')

