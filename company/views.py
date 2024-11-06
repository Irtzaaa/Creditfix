from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CompanyRegistrationForm

def register(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log the company in after registration
            login(request, user)
            return redirect('company_dashboard')  # Redirect to company dashboard or desired page
    else:
        form = CompanyRegistrationForm()
    return render(request, 'company/register.html', {'form': form})
from django.contrib.auth.forms import AuthenticationForm

def company_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('company_dashboard')  # Redirect to company dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'company/login.html', {'form': form})

def dashboard(request):
    return render(request, 'company/dashboard.html')
