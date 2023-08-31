from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('store')
    else:
        form = RegistrationForm()
              
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect('profile')
    
    return render(request, 'accounts/login.html')

def display_profile(request):
    return render(request, 'accounts/profile.html')

def user_logout(request):
    logout(request)
    return redirect('login')