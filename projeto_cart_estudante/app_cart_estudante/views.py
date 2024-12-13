from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Estudante

def home(request):
    if request.user.is_authenticated:  
        return redirect('estudantes\perfil_estudante.html')  
    if request.method == "POST":  
        username = request.POST['ra']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:  
            login(request, user)
            return redirect('estudantes\perfil_estudante.html')  
        else:
            return render(request, 'estudantes\home.html', {'error': 'Credenciais inválidas.'})
    return render(request, 'estudantes\home.html')  

@login_required
def perfil_estudante(request):
    estudante = get_object_or_404(Estudante, matricula=request.user.username)
    return render(request, 'estudantes\perfil_estudante.html', {'estudante': estudante})