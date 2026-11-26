from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def autenticacion(request):
    mensaje = ""
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(f"DATOS RECIBIDOS: Usuario: {username} | Contraseña: {password}")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # PASO CLAVE: iniciar sesión real en Django
            login(request, user)
            # PASO CLAVE: redirigir al dashboard
            return redirect('dashboard')
        else:
            mensaje = "Credenciales incorrectas. Intenta de nuevo."
    
    return render(request, 'app_auten/autenticacion.html', {'mensaje': mensaje})


# Vista protegida: solo usuarios autenticados pueden entrar
@login_required
def dashboard(request):
    return render(request, 'app_auten/dashboard.html', {'usuario': request.user})


def cerrar_sesion(request):
    logout(request)
    return redirect('autenticacion')