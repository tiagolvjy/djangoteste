from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = UserProfile.objects.filter(username=username, password=password).first()
        if user:
            # Usuário autenticado com sucesso
            messages.success(request, f'Bem-vindo, {username}!')
            return redirect('home')  # Redirecionar para a página inicial após o login
        else:
            # Credenciais inválidas
            messages.error(request, 'Credenciais inválidas. Tente novamente.')

    return render(request, 'accounts/login.html')
