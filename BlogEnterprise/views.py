from django.shortcuts import render # Necesario para renderizar templates

def home(request):
    return render(request, 'home.html') # Renderiza el template 'home.html'
