from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('daftar_mahasiswa')
        else:
            messages.error(request, 'Username atau password salah!')
    return render(request, 'accounts/login.html')

@login_required(login_url='/accounts/login/')
def logout_view(request):
    auth_logout(request)
    return redirect('login')

