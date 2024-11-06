from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'users/index.html')
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        
        if password == password_confirm:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
            else:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()
                messages.success(request, "Account created successfully.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'users/register.html')

# Login view
def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:dashboard')  # Redirect to a logged-in dashboard
        else:
            messages.error(request, "Invalid email or password.")
    return render(request, 'users/login.html')

# Logout view
def user_logout(request):
    logout(request)
    return redirect('login')

#@login_required
def dashboard(request):
    user_email = request.user.email  # Get the email of the current logged-in user
    return render(request, 'users/dashboard.html', {'email': user_email})

#@login_required
def credit_report(request):
    return render(request, 'users/credit_report.html')

#@login_required
def disputes(request):
    return render(request, 'users/disputes.html')

#@login_required
def setting(request):
    return render(request, 'users/setting.html')