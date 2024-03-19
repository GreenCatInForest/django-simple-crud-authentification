from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            # Check if user already exists
            if User.objects.filter(username=username).exists():
                print("User already exists")  # You can change this to redirect to a special page
                return redirect('special_page_url_name')  # Redirect to special page
            else:
                # Create new user
                user = User.objects.create(username=username, password=password, email=email)
                # Redirect to special page
                return redirect('special_page_url_name')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration_form.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('special_page_url_name')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home_page_url_name')  # Redirect to home page after logout

def home_page_url_name(request):
    return render(request, 'home_page_url_name.html')

@login_required
def special_page_url_name (request):
    return render(request, 'special_page_url_name.html')