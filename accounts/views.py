from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = RegistrationForm()
              
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    return render(request, 'accounts/login.html')