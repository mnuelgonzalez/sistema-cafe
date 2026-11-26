from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

def autenticacion(request):
    mensaje = ""
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(f"DATOS RECIBIDOS: Usuario: {username} | Contraseña: {password}")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            mensaje = "❌ Credenciales incorrectas. Intenta de nuevo."
    
    return render(request, 'app_auten/autenticacion.html', {'mensaje': mensaje})


@never_cache  # Capa 2: No guardar en caché
@login_required  # Capa 1: Proteger vista
def dashboard(request):
    return render(request, 'app_auten/dashboard.html', {'usuario': request.user})


@never_cache
def cerrar_sesion(request):
    logout(request)
    return redirect('autenticacion')