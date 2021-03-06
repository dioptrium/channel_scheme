from django.shortcuts import redirect, render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def main(request):
    return render(request, 'main/index.html')

def loginPage(request):
   
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect ('url_channels')
            else:
                messages.info(request, 'Имя или пароль неверны')
            
        context = {}
        return render(request, 'main/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
