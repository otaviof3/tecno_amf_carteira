from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .models import Estudante

def home(request):
    return render(request, "estudantes/home.html")

def perfil_estudante(request):
    matricula = request.session.get('matricula')
    if not matricula:
        return redirect('login')  
    estudante = get_object_or_404(Estudante, matricula=matricula)
    return render(request, 'perfil_estudante.html', {'estudante': estudante})

def login_view(request):
    if request.method == "POST":
        username = request.POST['matricula']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('perfil_estudante') 
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas.'})
    return render(request, 'login.html')